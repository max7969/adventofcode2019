import os
import file_utils
import math
from itertools import permutations


def extract_asteroids(map):
    asteroids = []
    for i in range (len(map)):
        for j in range (len(map[i])):
            if map[i][j] == "#":
                asteroids.append([j, i])       
    return asteroids

def vectorize(a, b):
    v1 = [0, -1]
    v2 = [b[0] - a[0], b[1] - a[1]]
    return v1, v2

def normalize(v):
    return math.sqrt(math.pow(v[0],2) + math.pow(v[1], 2))

def compute_angle(a, b):
    v1, v2 = vectorize(a, b)
    nv1, nv2 = normalize(v1), normalize(v2)
    cos = (v1[0] * v2[0] + v1[1] * v2[1]) / (nv1 * nv2)
    sin = (v1[0] * v2[1] - v1[1] * v2[0])
    return round(math.copysign(1, sin) * math.acos(cos), 4)

def find_angles(asteroids):
    max = 0
    point = asteroids[0]
    for asteroid in asteroids:
        angles = set()
        for asteroid_comparison in asteroids:
            if asteroid != asteroid_comparison:
                angles.add(compute_angle(asteroid, asteroid_comparison))
        if len(angles) > max:
            max = len(angles)
            point = asteroid
    return max, point


def solution(path_name, file_name):
    map = file_utils.get_lines(path_name, file_name)
    asteroids = extract_asteroids(map)
    max, point = find_angles(asteroids)
    return max


if __name__ == "__main__":
    print(solution("day10/inputs", "input"))

