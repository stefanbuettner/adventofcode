#!/bin/python

current_elf_nr = 1
wealthiest_elf_nr = 0
current_calories = 0
max_total_calories = 0
with open("input.txt") as f:
#with open("test_input.txt") as f:
    content = f.read()
    elves = content.split("\n\n")
    elves = [sum(map(int, elve.split())) for elve in elves]
    elves.sort(reverse=True)
    print(elves)
    print(elves[0] + elves[1] + elves[2])