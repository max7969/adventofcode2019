import os
import day12

def test1_day12():
    result = day12.solution("day12/inputs", "test_1", 10)
    assert result == 179

def test2_day12():
    result = day12.solution("day12/inputs", "test_2", 100)
    assert result == 1940