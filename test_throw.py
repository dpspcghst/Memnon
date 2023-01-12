from main import rps_throw

def test_throw():
    """
    """

    assert isinstance(rps_throw(), str)

if __name__ == "__main__":
    test_throw()
    print("Everything passed")
