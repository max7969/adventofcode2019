import os
import math

os.walk("/users/pc/data/adventofcode2019")


def base_path():
    return os.path.join("day1")


def solution(file_path):
    file = open(os.path.join(base_path(), file_path), "r")
    sum = 0
    for line in file.readlines():
        sum += math.floor(int(line.rstrip()) / 3.0) - 2
    return sum


def main():
    print(solution(os.path.join("inputs", "input")))


if __name__ == "__main__":
    main()
