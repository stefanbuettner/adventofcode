import math
import itertools as it
import functools as fn
import operator as op

example_times = [7, 15, 30]
example_records = [9, 40, 200]

input_times = [46, 80, 78, 66]
input_records = [214, 1177, 1402, 1024]

times = input_times
records = input_records

def faster(time, record, charging_time):
    return charging_time*(time - charging_time) - record

def charging_range(time, record):
    T_square = time * time
    offset = math.sqrt(T_square - 4.0 * record)
    min_charging_time = int(math.ceil((time - offset) / 2.0))
    max_charging_time = int(math.floor((time + offset) / 2.0))
    if faster(time, record, min_charging_time) < 1:
        min_charging_time += 1
    if faster(time, record, max_charging_time) < 1:
        max_charging_time -= 1
    return (min_charging_time, max_charging_time)

def charging_variance(min_time, max_time):
    return max_time - min_time + 1

def solve(times, records):
    # charging_ranges = list(map(charging_range, times, records))
    # print(charging_ranges)
    # variances = list(it.starmap(charging_variance, charging_ranges))
    # print(variances)
    return fn.reduce(op.mul, it.starmap(charging_variance, map(charging_range, times, records)))

print("Part 1: ", solve(times, records))

print("Part 2: ", solve([46807866], [214117714021024]))
