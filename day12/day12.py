import os
import file_utils
import math
import re

def extract_moons(lines):
    return [[int(line.group(1)), int(line.group(2)), int(line.group(3)), 0, 0, 0] for line in [re.search(r'<x=([\-0-9]*), y=([\-0-9]*), z=([\-0-9]*)>', line.rstrip()) for line in lines]]

def apply_gravity(moons):
    for moon in moons:
        for moon2 in moons:
            if moon != moon2:
                if moon[0] > moon2[0]:
                    moon[3] = moon[3] - 1
                elif moon[0] < moon2[0]:
                    moon[3] = moon[3] + 1
                if moon[1] > moon2[1]:
                    moon[4] = moon[4] - 1
                elif moon[1] < moon2[1]:
                    moon[4] = moon[4] + 1
                if moon[2] > moon2[2]:
                    moon[5] = moon[5] - 1
                elif moon[2] < moon2[2]:
                    moon[5] = moon[5] + 1
    return moons  

def apply_velocity(moons):
    for moon in moons:
        moon[0] = moon[0] + moon[3]
        moon[1] = moon[1] + moon[4]
        moon[2] = moon[2] + moon[5]
    return moons

def play_steps(moons, stepCount):
    for i in range(stepCount):
        moons = apply_gravity(moons)
        moons = apply_velocity(moons)
    return moons

def state_as_string(moons):
    return ",".join([str(moon) for moon in moons])

def find_repetiv_state(moons):
    states = set()
    initial, current = state_as_string(moons), ""
    count = 0
    while current != initial:
        moons = apply_gravity(moons)
        moons = apply_velocity(moons)
        current = state_as_string(moons)
        count = count + 1
        if count % 100000 == 0:
            print(count)
    return count

def compute_moon_energy(moon):
    return (abs(moon[0]) + abs(moon[1]) + abs(moon[2])) * (abs(moon[3]) + abs(moon[4]) + abs(moon[5]))

def compute_system_energy(moons):
    energy = 0
    for moon in moons:
        energy += compute_moon_energy(moon)
    return energy

def solution(path_name, file_name, stepCount):
    moons = extract_moons(file_utils.get_lines(path_name, file_name))
    moons = play_steps(moons, stepCount)
    return compute_system_energy(moons)

def solution2(path_name, file_name):
    moons = extract_moons(file_utils.get_lines(path_name, file_name))
    return find_repetiv_state(moons)

if __name__ == "__main__":
    print(solution("day12/inputs", "input", 1000))
    solution2("day12/inputs", "test_2")
   