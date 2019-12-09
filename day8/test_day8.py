import os
import day8


def test1_day8():
    layer, result = day8.solution(
        "day8/inputs", "test_1", "3x2", day8.best_layer)
    assert layer == 1
    assert result == 1
