import os
import re
import file_utils


def filter_following_numbers(passwords):
    filtered_passwords = set()
    regexps = [re.compile("[0-" + str(i) + "]*" + str(i) +
                          "{2,}[" + str(i) + "-9]*") for i in range(10)]
    for regexp in regexps:
        filtered_passwords = filtered_passwords.union(
            set(filter(regexp.fullmatch, passwords)))
    return list(filtered_passwords)


def filter_order(passwords):
    for password in passwords:
        if password[0] > password[1] or password[1] > password[2] or password[3] > password[4] or password[4] > password[5]:
            passwords.remove(password)
    return passwords


def possibilities(start, end):
    return [str(i) for i in range(start, end + 1)]


def solution(start, end):
    return len(filter_order(filter_following_numbers(possibilities(start, end))))


print(solution(172851, 675869))
