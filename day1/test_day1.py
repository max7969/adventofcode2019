import os
import day1


def test_day1():
    result = day1.solution("day1/inputs", "test_1")
    assert result == 34241


def test_day1_part2():
    result = day1.solution2("day1/inputs", "test_1")
    assert result == 51316
