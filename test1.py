from my_player_throw import player_throw
from settings import rps_throws

result = player_throw()

try:
    assert isinstance(result, str)
    print("string test passed (input() makes all input a string)")

except AssertionError:
    print("input wasn't a string")

try:
    assert result in rps_throws
    print("choice test passed")

except AssertionError:
    print("input wasn't paper, rock, or scissors")
