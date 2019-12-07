import os
import file_utils


def compute(program):
    memory = [int(i) for i in program.split(",")]
    addrOp = 0
    while memory[addrOp] != 99 or addrOp > (len(memory) - 1):
        param1, param2 = memory[memory[addrOp + 1]], memory[memory[addrOp + 2]]
        addrResult = memory[addrOp + 3]
        if memory[addrOp] == 1:
            memory[addrResult] = param1 + param2
        elif memory[addrOp] == 2:
            memory[addrResult] = param1 * param2
        addrOp = addrOp + 4
    return ",".join([str(i) for i in memory])


def fix_program(program, noun=12, verb=2):
    split = program.split(",")
    split[1] = str(noun)
    split[2] = str(verb)
    return ",".join(split)


def find_noun_and_verb(solution, program):
    for noun in range(100):
        for verb in range(100):
            if solution == int(compute(fix_program(program, noun, verb)).split(",")[0]):
                return str(100 * noun + verb)
    return "error"


def open_program(path_name, file_name):
    return file_utils.get_lines(path_name, file_name)[0]


def solution(path_name, file_name):
    program = fix_program(open_program(path_name, file_name))
    return compute(program).split(",")[0]


def solution2(path_name, file_name, solution):
    code = find_noun_and_verb(solution, open_program(path_name, file_name))
    return code


if __name__ == "__main__":
    print(solution("day2/inputs", "input"))
    print(solution2("day2/inputs", "input", 19690720))
