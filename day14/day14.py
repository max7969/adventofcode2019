import os
import file_utils
import math
import re


def classified_elements(reactions):
    classification = {}
    classification["ORE"] = 0
    step = 0
    while len(classification) <= len(reactions):
        step = step + 1
        added = []
        for reaction in reactions:
            if all(x in list(classification.keys()) for x in [element[1] for element in reaction[0]]):
                added.append(reaction[1][1])
        for add in added:
            if add not in classification.keys():
                classification[add] = step
    return classification


def compute_reactions(lines):
    key = r'([0-9]*)\ ([A-Z]*)'
    reactions = [
        [reaction[0].split(", "), reaction[1]]
        for reaction in [line.rstrip().split(" => ") for line in lines]]
    reactions = [[[re.search(key, element) for element in reaction[0]], re.search(key, reaction[1])]
                 for reaction in reactions]
    reactions = [[[[int(element.group(1)), element.group(2)] for element in reaction[0]],
                  [int(reaction[1].group(1)), reaction[1].group(2)]] for reaction in reactions]
    return reactions


def update_quantity_relicats_ratio(target, quantity, relicats):
    if target in relicats.keys():
        if quantity >= relicats[target]:
            quantity = quantity - relicats[target]
            relicats[target] = 0
        else:
            quantity = 0
            relicats[target] = relicats[target] - quantity
    return quantity, relicats


def find_reaction(target, reactions):
    for reaction in reactions:
        if reaction[1][1] == target:
            return reaction


def check_all_elements(elements, target):
    return len([element for element in elements if element[1] == target]) == len(elements)


def find_elements(quantity, target, reactions, relicats, classification):
    elements = []
    reaction = find_reaction(target, reactions)
    print(reaction[0])
    print(reaction[1])
    print(relicats)
    quantity, relicats = update_quantity_relicats_ratio(
        target, quantity, relicats)
    reactionCount = math.ceil(quantity / reaction[1][0])
    produced = reaction[1][0] * reactionCount
    needed = quantity
    elements.extend([[element[0] * reactionCount, element[1]]
                     for element in reaction[0]])
    if target in relicats.keys():
        relicats[target] += produced - needed
    else:
        relicats[target] = produced - needed

    elements = [[element[0], element[1], classification[element[1]]]
                for element in elements]
    elements = sorted(elements, key=lambda x: x[2], reverse=True)

    while check_all_elements(elements, "ORE") == False:
        for element in elements:
            if element[1] != "ORE":
                elements.remove(element)
                print(element[1] + ":" + str(element[0]))
                newElements, relicats = find_elements(
                    element[0], element[1], reactions, relicats, classification)
                elements.extend(newElements)
                break

    return elements, relicats


def solution(path_name, file_name):
    reactions = compute_reactions(file_utils.get_lines(path_name, file_name))
    classification = classified_elements(reactions)
    elements, relicats = find_elements(
        1, "FUEL", reactions, {}, classification)
    return sum([element[0] for element in elements])


if __name__ == "__main__":
    print(solution("day14/inputs", "input"))
