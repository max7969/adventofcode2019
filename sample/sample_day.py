import os

os.walk("/users/pc/data/adventofcode2019")


def base_path():
    return os.path.join("sample")


def solution(file_path):
    file = open(os.path.join(base_path(), file_path), "r")
    for line in file.readlines():
        print(line)
    return 0


def main():
    solution(os.path.join("inputs", "input_sample1"))


if __name__ == "__main__":
    main()
