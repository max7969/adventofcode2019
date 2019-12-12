import os
import file_utils
import math
import re


def extract_moons(lines):
    return [[int(line.group(1)), int(line.group(2)), int(line.group(3)), 0, 0, 0] for line in [re.search(r'<x=([\-0-9]*), y=([\-0-9]*), z=([\-0-9]*)>', line.rstrip()) for line in lines]]


def update_velocity(pos1, pos2, actual):
    if pos1 > pos2:
        actual = actual - 1
    elif pos1 < pos2:
        actual = actual + 1
    return actual


def apply_gravity(moons):
    for moon in moons:
        for moon2 in moons:
            if moon != moon2:
                moon[3] = update_velocity(moon[0], moon2[0], moon[3])
                moon[4] = update_velocity(moon[1], moon2[1], moon[4])
                moon[5] = update_velocity(moon[2], moon2[2], moon[5])
    return moons


def apply_velocity(moons):
    for moon in moons:
        moon[0] = moon[0] + moon[3]
        moon[1] = moon[1] + moon[4]
        moon[2] = moon[2] + moon[5]
    return moons


def play_steps(moons, stepCount):
    for _ in range(stepCount):
        moons = apply_gravity(moons)
        moons = apply_velocity(moons)
    return moons


def state_as_string(moons, index):
    return ",".join([str(moon[index]) + "," + str(moon[index + 3]) for moon in moons])


def find_recursivity(moons, index):
    initial, current = state_as_string(moons, index), ""
    count = 0
    while current != initial:
        moons = apply_gravity(moons)
        moons = apply_velocity(moons)
        current = state_as_string(moons, index)
        count = count + 1
    return count


def compute_moon_energy(moon):
    return (abs(moon[0]) + abs(moon[1]) + abs(moon[2])) * (abs(moon[3]) + abs(moon[4]) + abs(moon[5]))


def compute_system_energy(moons):
    return sum([compute_moon_energy(moon) for moon in moons])


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def ppcm(a, b):
    if (a == 0) or (b == 0):
        return 0
    else:
        return (a*b)//pgcd(a, b)


def solution(path_name, file_name, stepCount):
    moons = extract_moons(file_utils.get_lines(path_name, file_name))
    moons = play_steps(moons, stepCount)
    return compute_system_energy(moons)


def solution2(path_name, file_name):
    moons = extract_moons(file_utils.get_lines(path_name, file_name))
    x_cycle = find_recursivity(moons, 0)
    y_cycle = find_recursivity(moons, 1)
    z_cycle = find_recursivity(moons, 2)
    return ppcm(ppcm(x_cycle, y_cycle), z_cycle)


if __name__ == "__main__":
    print(solution("day12/inputs", "input", 1000))
    print(solution2("day12/inputs", "input"))
