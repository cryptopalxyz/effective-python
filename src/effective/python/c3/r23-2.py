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


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count


result, count = increment_with_report(current, increments)
assert count == 2
