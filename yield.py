#!/bin/usr/env python3


def __yield(initial_value, increment):
    i = initial_value
    while True:
        yield i
        i += increment

one = __yield(0, 1)
two = __yield(0, 5)

print(next(one))
print(next(one))
print(next(two))
print(next(one))
print(next(one))
print(next(two))
