import os
import day9


def test1_day9():
    result = day9.solution("day9/inputs", "test_1", 1)
    assert result == "1091204-1100110011001008100161011006101099"

def test2_day9():
    result = day9.solution("day9/inputs", "test_2", 1)
    assert len(result) == 16

def test3_day9():
    result = day9.solution("day9/inputs", "test_3", 1)
    assert result == "1125899906842624"