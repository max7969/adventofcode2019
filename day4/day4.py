import os
import re


def generate_regexp(constraint):
    return [re.compile("".join([str(j) + "*" for j in range(i)]) + str(i) +
                       constraint + "".join([str(j) + "*" for j in range(i + 1, 10)])) for i in range(10)]


def filter_passwords_softlty(passwords):
    filtered_passwords = set()
    for regexp in generate_regexp("{2,}"):
        filtered_passwords = filtered_passwords.union(
            set(filter(regexp.fullmatch, passwords)))
    return list(filtered_passwords)


def filter_passwords_strongly(passwords):
    passwords = filter_passwords_softlty(passwords)
    filtered_passwords = set()
    for regexp in generate_regexp("{2}"):
        filtered_passwords = filtered_passwords.union(
            set(filter(regexp.fullmatch, passwords)))
    return list(filtered_passwords)


def possibilities(start, end):
    return [str(i) for i in range(start, end + 1)]


def solution(start, end, filter):
    return len(filter(possibilities(start, end)))


if __name__ == "__main__":
    print(solution(172851, 675869, filter_passwords_softlty))
    print(solution(172851, 675869, filter_passwords_strongly))
