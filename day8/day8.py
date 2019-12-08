import os
import file_utils
from itertools import permutations


def get_layers(image, size):
    width, height = int(size.split("x")[0]), int(size.split("x")[1])
    layers, min, max = [], 0, width * height
    for i in range(int(len(image) / (width * height))):
        layers.append([int(image[i]) for i in range(min, max)])
        min, max = max, max + width * height
    return layers


def find_value_count(layer, value):
    return len(list(filter(lambda element: element == value, layer)))


def get_min_zero_value_layer(layers):
    min = len(layers[0])
    minLayer = layers[0]
    for layer in layers:
        zeroCount = find_value_count(layer, 0)
        if zeroCount < min:
            minLayer, min = layer, zeroCount
    return minLayer, layers.index(minLayer) + 1


def decode_image(layers, size):
    width, height = int(size.split("x")[0]), int(size.split("x")[1])
    image = []
    for i in range(width * height):
        for layer in layers:
            if layer[i] != 2:
                if layer[i] == 1:
                    image.append("X")
                else:
                    image.append(" ")
                break
    return image


def print_image(image, size):
    width, height = int(size.split("x")[0]), int(size.split("x")[1])
    lines = [image[x:x+width] for x in range(0, len(image), width)]
    for line in lines:
        print("".join([str(px) for px in line]))


def solution(path_name, file_name, size):
    image = file_utils.get_lines(path_name, file_name)[0]
    layers = get_layers(image, size)
    layer, layerNumber = get_min_zero_value_layer(layers)
    return layerNumber, find_value_count(layer, 1) * find_value_count(layer, 2)


def solution2(path_name, file_name, size):
    image = file_utils.get_lines(path_name, file_name)[0]
    layers = get_layers(image, size)
    image = decode_image(layers, size)
    print_image(image, size)


if __name__ == "__main__":
    print(solution("day8/inputs", "input", "25x6"))
    print(solution2("day8/inputs", "input", "25x6"))
