import os
import day10


def test1_day10():
    result, point = day10.solution("day10/inputs", "test_1")
    assert result == 8
    assert point == [3,4]

def test2_day10():
    result, point = day10.solution("day10/inputs", "test_2")
    assert result == 33
    assert point == [5,8]

def test3_day10():
    result, point = day10.solution("day10/inputs", "test_3")
    assert result == 35
    assert point == [1,2]

def test4_day10():
    result, point = day10.solution("day10/inputs", "test_4")
    assert result == 41
    assert point == [6,3]

def test5_day10():
    result, point = day10.solution("day10/inputs", "test_5")
    assert result == 210
    assert point == [11,13]

def test6_day10():
    angle = day10.compute_angle([0,0], [15,0])
    angle2 = day10.compute_angle([1,0], [25, 0])
    assert angle == angle2

def test7_day10():
    angle = day10.compute_angle([0,0], [-15,0])
    angle2 = day10.compute_angle([0,0], [-25, 0])
    assert angle == angle2

def test8_day10():
    angle = day10.compute_angle([0,0], [1,-1])
    angle2 = day10.compute_angle([0,0], [2, -2])
    assert angle == angle2