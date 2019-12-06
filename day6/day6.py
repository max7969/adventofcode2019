import os
import file_utils

def build_graph(lines):
    graph = {}
    for line in [line.rstrip() for line in lines]:
        parent, child = line.split(")")[0], line.split(")")[1]
        graph[child] = parent
    return graph

def count(parent, graph):
    leefs = [key for key in graph.keys() if key not in graph.values()]
    count = 0
    for current in leefs:
        while current != "COM":
            count += 1
            current = graph[current]
    return count


def solution(path_name, file_name):
    lines = file_utils.get_lines(path_name, file_name)
    graph = build_graph(lines)
    return count("COM", graph)

#print(solution("day6/inputs", "input"))
