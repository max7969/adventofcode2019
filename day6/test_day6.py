import os
import day6


def test1_day6():
    result = day6.solution("day6/inputs", "test_1", day6.count)
    assert result == 42


def test2_day6():
    result = day6.solution("day6/inputs", "test_2", day6.count_moves)
    assert result == 4
