import os
import math
import file_utils


def compute(program):
    instrs = [int(i) for i in program.split(",")]
    index = 0
    while instrs[index] != 99 or index > (len(instrs) - 1):
        if instrs[index] == 1:
            instrs[instrs[index + 3]] = instrs[instrs[index + 1]] + \
                instrs[instrs[index + 2]]
        elif instrs[index] == 2:
            instrs[instrs[index + 3]] = instrs[instrs[index + 1]] * \
                instrs[instrs[index + 2]]
        index = index + 4
    return ",".join([str(i) for i in instrs])


def fix_program(program, noun, verb):
    split = program.split(",")
    split[1] = str(noun)
    split[2] = str(verb)
    return ",".join(split)


def find_noun_and_verb(solution, program):
    for noun in range(100):
        for verb in range(100):
            fixed_program = fix_program(program, noun, verb)
            if solution == int(compute(fixed_program).split(",")[0]):
                return str(100 * noun + verb)
    return "error"


def open_program(path_name, file_name):
    return file_utils.get_lines(path_name, file_name)[0]


def solution(path_name, file_name):
    program = fix_program(open_program(path_name, file_name), 12, 2)
    return compute(program)


def solution2(path_name, file_name, solution):
    code = find_noun_and_verb(solution, open_program(path_name, file_name))
    return code


print(solution("day2/inputs", "input"))
print(solution2("day2/inputs", "input", 19690720))
