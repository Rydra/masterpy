from enum import Enum
import pytest

from validator import Validator, Result


class Colors(Enum):
    GREEN = 0
    RED = 1
    BLUE = 2



@pytest.mark.parametrize(
    "solution                       ,combination,                   expected_result", [
    ([Colors.GREEN, Colors.GREEN],  [Colors.GREEN, Colors.GREEN],   Result(black=2, white=0)),
    ([Colors.RED, Colors.RED],      [Colors.RED, Colors.RED],       Result(black=2, white=0)),
    ([Colors.RED, Colors.GREEN],    [Colors.RED, Colors.RED],       Result(black=1, white=0)),
    ([Colors.RED, Colors.GREEN],    [Colors.BLUE, Colors.BLUE],     Result(black=0, white=0)),
    ([Colors.BLUE, Colors.RED],    [Colors.RED, Colors.BLUE],     Result(black=0, white=2)),
])
def test_validate(solution, combination, expected_result):
    validator = Validator()
    assert validator.validate(solution, combination).black == expected_result.black
    assert validator.validate(solution, combination).white == expected_result.white
