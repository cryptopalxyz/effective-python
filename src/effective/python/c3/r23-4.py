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


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    # __call__ can make the class to be used as a function
    def __call__(self):
        self.added += 1
        return 0


better_counter = BetterCountMissing()

# decouple class and defaultdict
# assign class instance to the hook
result = defaultdict(better_counter, current)
for key, amount in increments:
    result[key] += amount
assert better_counter.added == 2
