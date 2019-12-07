import os
import math
import file_utils


def construct_wire(splitWire):
    coords = []
    currentX, currentY = 0, 0
    for exec in splitWire:
        dir = exec[0]
        step = int(exec[1:])
        if dir == "R":
            coords += generate_coords(currentX + 1,
                                      currentX + step + 1, currentY, currentY + 1)
            currentX = currentX + step
        elif dir == "L":
            coords += generate_coords(currentX - step,
                                      currentX, currentY, currentY + 1)[::-1]
            currentX = currentX - step
        elif dir == "U":
            coords += generate_coords(currentX, currentX + 1,
                                      currentY + 1, currentY + step + 1)
            currentY = currentY + step
        elif dir == "D":
            coords += generate_coords(currentX, currentX + 1,
                                      currentY - step, currentY)[::-1]
            currentY = currentY - step
    return coords


def manhattan_distance(commons):
    return [abs(int(common.split(",")[0])) + abs(int(common.split(",")[1])) for common in commons]


def power_distance(builded_wire1, builded_wire2, commons):
    return [cost(common, builded_wire1) + cost(common, builded_wire2) for common in commons]


def cost(common, wire):
    return wire.index(common) + 1


def generate_coords(startX, endX, startY, endY):
    coords = []
    for i in range(startX, endX):
        for j in range(startY, endY):
            coords.append(str(i) + "," + str(j))
    return coords


def closest(wire1, wire2):
    builded_wire1, builded_wire2 = construct_wire(
        wire1.split(",")), construct_wire(wire2.split(","))
    return min(manhattan_distance(list(set(builded_wire1).intersection(builded_wire2))))


def cheapest(wire1, wire2):
    builded_wire1, builded_wire2 = construct_wire(
        wire1.split(",")), construct_wire(wire2.split(","))
    return min(power_distance(builded_wire1, builded_wire2, list(set(builded_wire1).intersection(builded_wire2))))


def solution(path_name, file_name, cost_function):
    lines = file_utils.get_lines(path_name, file_name)
    return cost_function(lines[0], lines[1])


if __name__ == "__main__":
    print(solution("day3/inputs", "input", closest))
    print(solution("day3/inputs", "input", cheapest))
