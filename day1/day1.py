import os
import math
from lib import file_utils


def fuel_per_module(weight):
    return (math.trunc(weight / 3.0) - 2)


def fuel_per_module2(weight):
    fuel = fuel_per_module(weight)
    additional_fuel = fuel_per_module(fuel)
    while additional_fuel > 0:
        fuel += additional_fuel
        additional_fuel = fuel_per_module(additional_fuel)
    return fuel


def compute(lines, fuel_function):
    sum = 0
    for line in lines:
        sum += fuel_function(int(line.rstrip()))
    return sum


def solution(path_name, file_name):
    return compute(file_utils.get_lines(path_name, file_name), fuel_per_module)


def solution2(path_name, file_name):
    return compute(file_utils.get_lines(path_name, file_name), fuel_per_module2)
