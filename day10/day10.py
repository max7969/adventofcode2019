import os
import file_utils
import math
from itertools import permutations
import time


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
    angle = round(math.copysign(1, sin) * math.acos(cos), 4)
    if angle >= 0:
        return angle
    else:
        return round(math.pi*2 + angle, 4)

def dist(center, asteroid):
    return abs(center[0] - asteroid[0]) + abs(center[1] - asteroid[1])

def find_angles(center, asteroids):
    angles = []
    for asteroid in asteroids:
        if center != asteroid:
            angles.append([compute_angle(center, asteroid), dist(center, asteroid), asteroid])
    return angles

def find_best_asteroid(asteroids):
    max, center, possible_angles = 0, asteroids[0], []
    for asteroid in asteroids:
        angles = set([element[0] for element in find_angles(asteroid, asteroids)])
        if len(angles) > max:
            max = len(angles)
            center = asteroid
            possible_angles = angles
    return max, center, possible_angles

def find_200th_destroyed_asteroid(asteroids):
    _, center, possible_angles = find_best_asteroid(asteroids)
    angles = find_angles(center, asteroids)
    possible_angles = sorted(angles, key=lambda x: x)
    angles = sorted(angles, key=lambda x: (x[0], x[1], x[0]))
    value = angles[0][0]
    count = 0
    for angle in angles:
        if angle[0] == value:
            angle.append(count)
            count += 1
        else:
            value = angle[0]
            count = 0
            angle.append(count)
    angles = sorted(angles, key=lambda x: (x[3], x[0]))
    return angles[199][2][0] * 100 + angles[199][2][1]

def solution(path_name, file_name, function):
    map = file_utils.get_lines(path_name, file_name)
    asteroids = extract_asteroids(map)
    return function(asteroids)


if __name__ == "__main__":
    start_time = time.time()
    #print(solution("day10/inputs", "input", find_best_asteroid))
    print(solution("day10/inputs", "input", find_200th_destroyed_asteroid))
    print("--- %s seconds ---" % (time.time() - start_time))

