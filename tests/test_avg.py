import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from avg import average_of_five


def test_simple():
    assert average_of_five([1, 2, 3, 4, 5]) == 3.0


def test_all_same():
    assert average_of_five([2, 2, 2, 2, 2]) == 2.0


def test_negative():
    assert average_of_five([-1, -2, -3, -4, -5]) == -3.0
