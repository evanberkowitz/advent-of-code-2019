#!/usr/bin/env python3

input="input"

total = 0
with open(input) as spacecraft:
    for module in spacecraft:
        mass = int(module)
        fuel = (mass // 3) - 2
        total += fuel

print(total)
