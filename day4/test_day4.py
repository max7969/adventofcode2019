import os
import day4


def test1_day4():
    assert len(day4.filter_passwords(["223450"])) == 0

def test2_day4():
    assert len(day4.filter_passwords(["111111"])) == 1

def test3_day4():
    assert len(day4.filter_passwords(["123789"])) == 0

def test4_day4():
    assert len(day4.filter_passwords_2(["112233"])) == 1

def test5_day4():
    assert len(day4.filter_passwords_2(["123444"])) == 0

def test6_day4():
    assert len(day4.filter_passwords_2(["111122"])) == 1