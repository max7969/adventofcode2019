import os
import day7


def test1_day7():
    signal, code = day7.solution("day7/inputs", "test_1", 0, "01234")
    assert signal == 43210
    assert code == ('4', '3', '2', '1', '0')


def test2_day7():
    signal, code = day7.solution("day7/inputs", "test_2", 0, "56789")
    assert signal == 139629729
    assert code == ('9', '8', '7', '6', '5')


def test3_day7():
    signal, code = day7.solution("day7/inputs", "test_3", 0, "56789")
    assert signal == 18216
    assert code == ('9', '7', '8', '5', '6')
