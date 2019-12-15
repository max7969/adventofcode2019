import os
import day14


def test1_day14():
    result = day14.solution("day14/inputs", "test_1")
    assert result == 31


def test2_day14():
    result = day14.solution("day14/inputs", "test_2")
    assert result == 165


def test3_day14():
    result = day14.solution("day14/inputs", "test_3")
    assert result == 13312


def test4_day14():
    result = day14.solution("day14/inputs", "test_4")
    assert result == 180697


def test5_day14():
    result = day14.solution("day14/inputs", "test_5")
    assert result == 2210736
