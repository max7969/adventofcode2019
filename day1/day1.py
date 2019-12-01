import os
import math

os.walk("/users/pc/data/adventofcode2019")


def base_path():
    return os.path.join("day1")


def get_lines(file_path):
    file = open(os.path.join(base_path(), file_path), "r")
    return file.readlines()


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


def solution(file_path):
    return compute(get_lines(file_path), fuel_per_module)


def solution2(file_path):
    return compute(get_lines(file_path), fuel_per_module2)


def main():
    print(solution(os.path.join("inputs", "input")))
    print(solution2(os.path.join("inputs", "input")))


if __name__ == "__main__":
    main()
