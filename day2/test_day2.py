import os
import day2


def test1_day2():
    result = day2.compute("1,0,0,0,99")
    assert result == "2,0,0,0,99"


def test2_day2():
    result = day2.compute("2,3,0,3,99")
    assert result == "2,3,0,6,99"


def test3_day2():
    result = day2.compute("2,4,4,5,99,0")
    assert result == "2,4,4,5,99,9801"


def test4_day2():
    result = day2.compute("1,1,1,4,99,5,6,0,99")
    assert result == "30,1,1,4,2,5,6,0,99"


def test5_day2():
    program = day2.fix_program("0,0,0,0", 12, 2)
    assert program == "0,12,2,0"


def test6_day2():
    solution = day2.find_noun_and_verb(
        2890696, day2.open_program("day2/inputs", "input"))
    assert solution == "1202"
