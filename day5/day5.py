import os
import file_utils


def compute(program, input):
    memory = [int(i) for i in program.split(",")]
    addrOp = 0
    output = ""
    while memory[addrOp] != 99 or addrOp > (len(memory) - 1):
        step = 2
        if memory[addrOp] == 3:
            memory[memory[addrOp + 1]] = input
        else:
            op, mode1, mode2, mode3 = read_op(memory[addrOp])
            addr1, addr2, addr3 = get_addrs(
                mode1, mode2, mode3, memory, addrOp)
            if op == 4:
                step = 2
                output += str(memory[addr1])
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
    return int(output)


def read_op(code):
    op = code % 100
    mode1 = ((code % 1000) - op) / 100
    mode2 = ((code % 10000) - mode1*100 - op) / 1000
    mode3 = ((code % 100000) - mode2*1000 - mode1*100 - op) / 10000
    return op, int(mode1), int(mode2), int(mode3)


def get_addrs(mode1, mode2, mode3, memory, addrOp):
    addr1, addr2, addr3 = 0, 0, 0
    if mode1 == 0:
        addr1 = memory[addrOp + 1]
    else:
        addr1 = addrOp + 1

    if mode2 == 0:
        addr2 = memory[addrOp + 2]
    else:
        addr2 = addrOp + 2

    if mode3 == 0:
        addr3 = memory[addrOp + 3]
    else:
        addr3 = addrOp + 3
    return addr1, addr2, addr3


def open_program(path_name, file_name):
    return file_utils.get_lines(path_name, file_name)[0]


def solution(path_name, file_name, input):
    return compute(open_program(path_name, file_name), input)


if __name__ == "__main__":
    print(solution("day5/inputs", "input", 1))
    print(solution("day5/inputs", "input", 5))
