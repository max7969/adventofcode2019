import os
import file_utils


def build_graph(lines):
    graph = {}
    for line in [line.rstrip() for line in lines]:
        parent, child = line.split(")")[0], line.split(")")[1]
        graph[child] = parent
    return graph


def create_path_to_com(current, graph):
    path = []
    while current != "COM":
        path.append(graph[current])
        current = graph[current]
    return path


def count(parent, graph):
    total, deep = 0, 1
    parents, nextLayer = [parent], []
    for i in range(len(graph)):
        for key, val in graph.items():
            if val in parents:
                total += deep
                nextLayer.append(key)
        deep += 1
        parents, nextLayer = nextLayer, []
    return total


def count_moves(parent, graph):
    pathYou, pathSan = create_path_to_com(
        "YOU", graph), create_path_to_com("SAN", graph)
    common = find_first_common(pathYou, pathSan)
    countYou, countSan = count_to_target(
        pathYou, common), count_to_target(pathSan, common)
    return countYou + countSan


def find_first_common(path1, path2):
    for element in path1:
        if element in path2:
            return element
    return "error"


def count_to_target(path, target):
    count = 0
    for element in path:
        if element == target:
            return count
        count += 1


def solution(path_name, file_name, function):
    lines = file_utils.get_lines(path_name, file_name)
    graph = build_graph(lines)
    return function("COM", graph)


print(solution("day6/inputs", "input", count))
print(solution("day6/inputs", "input", count_moves))
