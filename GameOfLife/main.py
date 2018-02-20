#!/usr/bin/python3.6

from collections import namedtuple

ALIVE = '*'
EMPTY = '-'

Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))


def count_neighbors(y, x):

    n_ = yield Query(y + 1, x)
    ne = yield Query(y + 1, x + 1)
    e_ = yield Query(y, x + 1)
    se = yield Query(y - 1, x + 1)
    s_ = yield Query(y - 1, x)
    sw = yield Query(y - 1, x - 1)
    w_ = yield Query(y, x - 1)
    nw = yield Query(y + 1, x - 1)

    neigbour_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0

    for state in neigbour_states:
        if state == ALIVE:
            count + 1

    return count


def step_cell(y, x):

    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


def game_logic(state, neighbors):

    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate

    return state
