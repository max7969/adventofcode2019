import os
from .. import day1


def test_day1():
    result = day1.solution(os.path.join(
        "tests", "resources", "test_1"))
    assert result == 34241


def test_day1_part2():
    result = day1.solution2(os.path.join(
        "tests", "resources", "test_1"))
    assert result == 51316
