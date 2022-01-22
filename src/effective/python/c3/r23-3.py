# -*- coding: utf-8 -*-
from collections import defaultdict

# a hook for default value
# use closure as  a hook

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()

result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount
assert counter.added == 2