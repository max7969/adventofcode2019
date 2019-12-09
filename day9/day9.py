import os
import file_utils
from itertools import permutations


def program_from_memory(memory):
    return ",".join([str(i) for i in memory])


def move_addrop(addrOp, step):
    return addrOp + step


def compute(program, inputs, addrOp):
    memory = [int(i) for i in program.split(",")]
    output = ""
    relativeBase = 0
    while memory[addrOp] != 99 or addrOp > (len(memory) - 1):
        op, mode1, mode2, mode3 = read_op(memory[addrOp])
        addr1, addr2, addr3 = get_addrs(
            mode1, mode2, mode3, memory, addrOp, relativeBase)

        if op == 3:
            memory[addr1] = inputs[0]
            inputs.pop(0)
            addrOp = move_addrop(addrOp, 2)
        elif op == 4:
            addrOp = move_addrop(addrOp, 2)
            inputs.append(memory[addr1])
            output += str(memory[addr1])
        elif op == 1:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(memory, addr3)
            memory[addr3] = memory[addr1] + memory[addr2]
        elif op == 2:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(memory, addr3)
            memory[addr3] = memory[addr1] * memory[addr2]
        elif op == 5:
            if memory[addr1] != 0:
                addrOp = memory[addr2]
            else:
                addrOp = move_addrop(addrOp, 3)
        elif op == 6:
            if memory[addr1] == 0:
                addrOp = memory[addr2]
            else:
                addrOp = move_addrop(addrOp, 3)
        elif op == 7:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(memory, addr3)
            if memory[addr1] < memory[addr2]:
                memory[addr3] = 1
            else:
                memory[addr3] = 0
        elif op == 8:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(memory, addr3)
            if memory[addr2] == memory[addr1]:
                memory[addr3] = 1
            else:
                memory[addr3] = 0
        elif op == 9:
            addrOp = move_addrop(addrOp, 2)
            relativeBase += memory[addr1]
    return output


def read_op(code):
    op = code % 100
    mode1 = ((code % 1000) - op) / 100
    mode2 = ((code % 10000) - mode1*100 - op) / 1000
    mode3 = ((code % 100000) - mode2*1000 - mode1*100 - op) / 10000
    return op, int(mode1), int(mode2), int(mode3)

def extend_memory_if_needed(memory, addr):
    if addr >= len(memory):
        for i in range(len(memory), addr + 1):
            memory.append(0)
    return memory

def get_addrs(mode1, mode2, mode3, memory, addrOp, relativeBase):
    addr1, addr2, addr3 = 0, 0, 0
    if mode1 == 0 and addrOp + 1 < len(memory):
        addr1 = memory[addrOp + 1]
    elif mode1 == 1:
        addr1 = addrOp + 1
    elif mode1 == 2 and addrOp + 1 < len(memory):
        addr1 = memory[addrOp + 1] + relativeBase

    if mode2 == 0 and addrOp + 2 < len(memory):
        addr2 = memory[addrOp + 2]
    elif mode2 == 1:
        addr2 = addrOp + 2
    elif mode2 == 2 and addrOp + 2 < len(memory):
        addr2 = memory[addrOp + 2] + relativeBase

    if mode3 == 0 and addrOp + 3 < len(memory):
        addr3 = memory[addrOp + 3]
    elif mode3 == 1:
        addr3 = addrOp + 3
    elif mode3 == 2 and addrOp + 3 < len(memory):
        addr3 = memory[addrOp + 3] + relativeBase
    return addr1, addr2, addr3


def open_program(path_name, file_name):
    return file_utils.get_lines(path_name, file_name)[0]


def solution(path_name, file_name, input):
    program = open_program(path_name, file_name)
    return compute(program, [input], 0)


if __name__ == "__main__":
    print(solution("day9/inputs", "input", 1))
    print(solution("day9/inputs", "input", 2))
