"""
    This module introduces the assert keyword.
"""

if __name__ == "__assert__":
    try:
        assert 10 == int("10")
        assert 5 == 10, "Sorry, 5 does not equal 10. =("
        # if not 5 == 10:
        #     raise AssertionError("Sorry, 5 does not equal 10. =(")

    except AssertionError as error:
        print(error)
