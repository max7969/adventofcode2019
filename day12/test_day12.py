import os
import day12


def test1_day12():
    result = day12.solution("day12/inputs", "test_1", 10)
    assert result == 179


def test2_day12():
    result = day12.solution("day12/inputs", "test_2", 100)
    assert result == 1940


def test3_day12():
    result = day12.solution2("day12/inputs", "test_1")
    assert result == 2772


def test4_day2():
    result = day12.solution2("day12/inputs", "test_2")
    assert result == 4686774924


def test5_day12():
    result = day12.pgcd(56, 42)
    assert result == 14
