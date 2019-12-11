import os
import day11


def test1_day11():
    paintedWhite, paintedBlack = day11.move_robot(
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
    assert len(paintedWhite) == 5
    assert len(paintedBlack) == 2
    paintedWhite.extend(paintedBlack)
    assert len(set([str(element[0]) + "," + str(element[1])
                    for element in paintedWhite])) == 6
