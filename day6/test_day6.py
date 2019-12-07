import os
import day6


def test1_day6():
    result = day6.solution("day6/inputs", "test_1")
    assert result == 42


def test2_day6():
    result = day6.solution2("day6/inputs", "test_2")
    assert result == 4
