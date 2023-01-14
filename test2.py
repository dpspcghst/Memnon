from my_rps_throw import rps_throw

result = rps_throw()

try:
    assert isinstance(result, str)
    print("test passed")

except AssertionError:
    print("input wasn't a string")
