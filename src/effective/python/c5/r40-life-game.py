# -*- coding: utf-8 -*-
from collections import namedtuple

ALIVE = '*'
EMPTY = '-'

Query = namedtuple('Query', ('y', 'x'))


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0) # North
    ne = yield Query(y + 1, x + 1) # Northeast
    e_ = yield Query(y + 0, x + 1) # East
    se = yield Query(y - 1, x + 1) # Southeast
    s_ = yield Query(y - 1, x + 0) # South
    sw = yield Query(y - 1, x - 1) # Southwest
    w_ = yield Query(y + 0, x - 1) # West
    nw = yield Query(y + 1, x - 1) # Northwest
    neighbor_starts = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_starts:
        if state == ALIVE:
            count += 1
    return count

it = count_neighbors(10, 5)
q1 = next(it)
print('First yield: ', q1)
q2 = it.send(ALIVE)  # send q1 state, get q2
print('Second yield: ', q2)
q3 = it.send(ALIVE)

try:
    count = it.send(EMPTY)
except StopIteration as e:
    print('Count: ', e.value)

Transition = namedtuple('Transition', ('y', 'x', 'state'))


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors> 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state

def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)

it = step_cell(10, 5)
q0 = next(it)
print('Me: ', q0)
q1 = it.send(ALIVE)  # send q1 state, get q2
print('Q1 : ', q1)
q2 = it.send(ALIVE)
print('Q2 : ', q2)
q3 = it.send(ALIVE)
print('Q2 : ', q3)
q4 = it.send(ALIVE)
print('Q2 : ', q4)
q5 = it.send(ALIVE)
print('Q2 : ', q5)
q6 = it.send(ALIVE)
print('Q2 : ', q6)
q7 = it.send(ALIVE)
print('Q2 : ', q7)
q8 = it.send(ALIVE)
print('Q2 : ', q8)
t1 = it.send(EMPTY)
print('Outcome: ', t1)

TICK = object()

def simulate(grid):
    next_grid = Grid(grid.height, grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(y, x, grid.get, next_grid.set)
    return next_grid

class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output

    def query(self, y, x):
        return self.rows[ y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny

grid = Grid(5, 9)
grid.assign(0, 3, ALIVE)
print(grid)

