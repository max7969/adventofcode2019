import os
import file_utils
import time
from itertools import permutations


def clear(): return os.system('clear')  # on Linux System


def program_from_memory(memory):
    return ",".join([str(i) for i in memory])


def move_addrop(addrOp, step):
    return addrOp + step


def compute(program, inputs, addrOp):
    memory = [int(i) for i in program.split(",")]
    output = []
    relativeBase = 0
    countOp = 0
    current, dir = [0, 0], [0, -1]
    painted = {}
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
            output.append(memory[addr1])
            if countOp % 2 == 1:
                painted[str(current[0]) + "," + str(current[1])
                        ] = output[countOp - 1]
                dir, current = move_robot(current, dir, output[countOp])
                if (str(current[0]) + "," + str(current[1])) in painted.keys():
                    inputs.append(
                        painted[str(current[0]) + "," + str(current[1])])
                else:
                    inputs.append(0)
            countOp = countOp + 1
        elif op == 1:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(
                memory, max([addr1, addr2, addr3]))
            memory[addr3] = memory[addr1] + memory[addr2]
        elif op == 2:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(
                memory,  max([addr1, addr2, addr3]))
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
            memory = extend_memory_if_needed(
                memory,  max([addr1, addr2, addr3]))
            if memory[addr1] < memory[addr2]:
                memory[addr3] = 1
            else:
                memory[addr3] = 0
        elif op == 8:
            addrOp = move_addrop(addrOp, 4)
            memory = extend_memory_if_needed(
                memory,  max([addr1, addr2, addr3]))
            if memory[addr2] == memory[addr1]:
                memory[addr3] = 1
            else:
                memory[addr3] = 0
        elif op == 9:
            addrOp = move_addrop(addrOp, 2)
            relativeBase += memory[addr1]
    return painted


def read_op(code):
    op = code % 100
    mode1 = ((code % 1000) - op) / 100
    mode2 = ((code % 10000) - mode1*100 - op) / 1000
    mode3 = ((code % 100000) - mode2*1000 - mode1*100 - op) / 10000
    return op, int(mode1), int(mode2), int(mode3)


def extend_memory_if_needed(memory, addr):
    if addr >= len(memory):
        for _ in range(len(memory), addr + 1):
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


def get_next_dir(dir, instruction):
    if instruction == 0:
        if dir == [0, -1]:
            return [-1, 0]
        elif dir == [-1, 0]:
            return [0, 1]
        elif dir == [0, 1]:
            return [1, 0]
        elif dir == [1, 0]:
            return [0, -1]
    elif instruction == 1:
        if dir == [0, -1]:
            return [1, 0]
        elif dir == [1, 0]:
            return [0, 1]
        elif dir == [0, 1]:
            return [-1, 0]
        elif dir == [-1, 0]:
            return [0, -1]


def move_robot(pos, dir, instruction):
    dir = get_next_dir(dir, instruction)
    return dir, [pos[0] + dir[0], pos[1] + dir[1]]


def print_robot(painted):
    minX = min([int(key.split(",")[0]) for key in painted])
    maxX = max([int(key.split(",")[0]) for key in painted])
    minY = min([int(key.split(",")[1]) for key in painted])
    maxY = max([int(key.split(",")[1]) for key in painted])

    for j in range(minY, maxY + 1):
        line = ""
        for i in range(minX, maxX + 1):
            if (str(i) + "," + str(j)) in painted.keys() and painted[str(i) + "," + str(j)] == 1:
                line += "#"
            else:
                line += " "
        print(line)


def solution(path_name, file_name, input):
    program = open_program(path_name, file_name)
    painted = compute(program, [input], 0)
    print_robot(painted)
    return len(painted)


if __name__ == "__main__":
    print(solution("day11/inputs", "input", 0))
    print(solution("day11/inputs", "input", 1))
