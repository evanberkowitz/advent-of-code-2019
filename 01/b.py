#!/usr/bin/env python3

input="input"

total = 0
with open(input) as spacecraft:
    for module in spacecraft:
        mass = int(module)
        fuel = (mass // 3) - 2
        while(fuel > 0):
            total += fuel
            fuel = (fuel // 3) - 2

print(total)
