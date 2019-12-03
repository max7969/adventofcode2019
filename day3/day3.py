import os
import math
import file_utils

def construct_wire(splitWire):
    coords = []
    currentX = 0
    currentY = 0
    for exec in splitWire:
        dir = exec[0]
        step = int(exec[1:])
        if dir == "R":
            coords += generate_coords(currentX + 1, currentX + step + 1, currentY, currentY + 1)
            currentX = currentX + step
        elif dir == "L":
            coords += generate_coords(currentX - step, currentX, currentY, currentY + 1)
            currentX = currentX - step
        elif dir == "U":
            coords += generate_coords(currentX, currentX + 1, currentY + 1, currentY + step + 1)
            currentY = currentY + step
        elif dir == "D":
            coords += generate_coords(currentX, currentX + 1, currentY - step, currentY)
            currentY = currentY - step
    return coords

def manhattan_distance(commons):
    commons = [abs(int(common.split(",")[0])) + abs(int(common.split(",")[1])) for common in commons]
    return commons

def generate_coords(startX, endX, startY, endY):
    coords = []
    for i in range(startX, endX):
        for j in range(startY, endY):
            coords.append(str(i) + "," + str(j))
    return coords

def closest(wire1, wire2):
    builded_wire1 = construct_wire(wire1.split(","))
    builded_wire2 = construct_wire(wire2.split(","))
    commons = list(set(builded_wire1).intersection(builded_wire2))
    return min(manhattan_distance(commons))


def solution(path_name, file_name):
    lines = file_utils.get_lines(path_name, file_name)
    return closest(lines[0], lines[1])

