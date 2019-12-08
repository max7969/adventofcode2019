import os
import file_utils
from itertools import permutations


def convert_size(size):
    width, height = int(size.split("x")[0]), int(size.split("x")[1])
    return width, height, width * height


def get_layers(image, size):
    _, _, pxCount = convert_size(size)
    layers, min, max = [], 0, pxCount
    for _ in range(int(len(image) / (pxCount))):
        layers.append([int(image[i]) for i in range(min, max)])
        min, max = max, max + pxCount
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


def decode_image(layers, pxCount):
    return [str(list(filter(lambda px: px != 2, pxValues))[0]).replace("1", "X").replace("0", " ") for pxValues in [
        [layer[i] for layer in layers] for i in range(pxCount)]]


def print_image(layers, size):
    width, _, pxCount = convert_size(size)
    image = decode_image(layers, pxCount)
    lines = [image[x:x+width] for x in range(0, len(image), width)]
    printed_image = ""
    for line in lines:
        printed_image += "".join([str(px) for px in line]) + "\n"
    return printed_image


def best_layer(layers, size):
    layer, layerNumber = get_min_zero_value_layer(layers)
    return layerNumber, find_value_count(layer, 1) * find_value_count(layer, 2)


def solution(path_name, file_name, size, layer_function):
    image = file_utils.get_lines(path_name, file_name)[0]
    layers = get_layers(image, size)
    return layer_function(layers, size)


if __name__ == "__main__":
    print(solution("day8/inputs", "input", "25x6", best_layer))
    print(solution("day8/inputs", "input", "25x6", print_image))
