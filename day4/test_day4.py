import os
import day4


def test1_day4():
    assert len(day4.filter_passwords_softlty(["223450"])) == 0


def test2_day4():
    assert len(day4.filter_passwords_softlty(["111111"])) == 1


def test3_day4():
    assert len(day4.filter_passwords_softlty(["123789"])) == 0


def test4_day4():
    assert len(day4.filter_passwords_strongly(["112233"])) == 1


def test5_day4():
    assert len(day4.filter_passwords_strongly(["123444"])) == 0


def test6_day4():
    assert len(day4.filter_passwords_strongly(["111122"])) == 1
