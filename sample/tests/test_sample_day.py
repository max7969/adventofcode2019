import os
from .. import sample_day


def test_sample():
    sample_day.solution(os.path.join(
        "tests", "resources", "sample_input_test_1"))
