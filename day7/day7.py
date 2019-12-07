import os
import file_utils
from itertools import permutations


def compute(program, inputs, addrOp):
    memory = [int(i) for i in program.split(",")]
    while memory[addrOp] != 99 or addrOp > (len(memory) - 1):
        step = 0
        op, mode1, mode2, mode3 = read_op(memory[addrOp])
        addr1, addr2, addr3 = get_addrs(
            mode1, mode2, mode3, memory, addrOp)
        if op == 3:
            step = 2
            memory[memory[addrOp + 1]] = inputs[0]
            inputs.pop(0)
        if op == 4:
            step = 2
            return inputs, 3, ",".join([str(i) for i in memory]), addrOp + step, memory[addr1]
        elif op == 1:
            memory[addr3] = memory[addr1] + memory[addr2]
            step = 4
        elif op == 2:
            memory[addr3] = memory[addr1] * memory[addr2]
            step = 4
        elif op == 5:
            if memory[addr1] != 0:
                step = 0
                addrOp = memory[addr2]
            else:
                step = 3
        elif op == 6:
            if memory[addr1] == 0:
                step = 0
                addrOp = memory[addr2]
            else:
                step = 3
        elif op == 7:
            step = 4
            if memory[addr1] < memory[addr2]:
                memory[addr3] = 1
            else:
                memory[addr3] = 0
        elif op == 8:
            step = 4
            if memory[addr2] == memory[addr1]:
                memory[addr3] = 1
            else:
                memory[addr3] = 0

        addrOp = addrOp + step
    return [0], 99, ",".join([str(i) for i in memory]), addrOp, 0


def read_op(code):
    op = code % 100
    mode1 = ((code % 1000) - op) / 100
    mode2 = ((code % 10000) - mode1*100 - op) / 1000
    mode3 = ((code % 100000) - mode2*1000 - mode1*100 - op) / 10000
    return op, int(mode1), int(mode2), int(mode3)


def get_addrs(mode1, mode2, mode3, memory, addrOp):
    addr1, addr2, addr3 = 0, 0, 0
    if mode1 == 0 and addrOp + 1 < len(memory):
        addr1 = memory[addrOp + 1]
    else:
        addr1 = addrOp + 1

    if mode2 == 0 and addrOp + 2 < len(memory):
        addr2 = memory[addrOp + 2]
    else:
        addr2 = addrOp + 2

    if mode3 == 0 and addrOp + 3 < len(memory):
        addr3 = memory[addrOp + 3]
    else:
        addr3 = addrOp + 3
    return addr1, addr2, addr3


def possibilities(phase_mode):
    return set(permutations(phase_mode))


def open_program(path_name, file_name):
    return file_utils.get_lines(path_name, file_name)[0]


def simple_mode(program, code, input):
    for element in code:
        nextInputs, codeStop, program, addrOp, input = compute(
            program, [int(element), input], 0)
    return input


def loop_mode(program, code, input):
    previousOutput = input
    codeStops = []
    codePrograms = {}
    lastOutput = 0
    for element in code:
        codePrograms[element] = [program, previousOutput, [int(element)]]
    while 99 not in codeStops:
        codeStops = []
        for element in code:
            codePrograms[element][2].append(previousOutput)
            nextInputs, codeStop, program, addrOp, previousOutput = compute(
                codePrograms[element][0], codePrograms[element][2], codePrograms[element][1])
            codePrograms[element][0] = program
            codePrograms[element][1] = addrOp
            codePrograms[element][2] = nextInputs
            codeStops.append(codeStop)
            if codeStop == 99:
                break
            if element == code[4]:
                lastOutput = previousOutput
    return lastOutput


def solution(path_name, file_name, input, phase_mode):
    codesToTry = possibilities(phase_mode)
    program = open_program(path_name, file_name)
    max, goodCode = 0, list(codesToTry)[0]
    for code in codesToTry:
        if phase_mode == "01234":
            signal = simple_mode(program, code, input)
        elif phase_mode == "56789":
            signal = loop_mode(program, code, input)
        if signal > max:
            max, goodCode = signal, code
    return max, goodCode


if __name__ == "__main__":
    print(solution("day7/inputs", "input", 0, "01234"))
    print(solution("day7/inputs", "input", 0, "56789"))
