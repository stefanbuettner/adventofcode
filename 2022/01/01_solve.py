#!/bin/python

current_elf_nr = 1
wealthiest_elf_nr = 0
current_calories = 0
max_total_calories = 0
with open("input.txt") as f:
#with open("test_input.txt") as f:
    for line in f:
        line = line.strip()
        print(line)
        if line == "":
            if max_total_calories < current_calories:
                wealthiest_elf_nr = current_elf_nr
                max_total_calories = current_calories
            current_calories = 0
            current_elf_nr += 1
        else:
            current_calories += int(line)

if max_total_calories < current_calories:
    wealthiest_elf_nr = current_elf_nr
    max_total_calories = current_calories

print("Elf: {}".format(wealthiest_elf_nr))
print("Calories: {}".format(max_total_calories))
