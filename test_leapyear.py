import pytest
import leapyear

class TestLeapyear:
    def test(self):
        #first test
        assert leapyear.leapyear(4) == "4 is a leap year"
        assert leapyear.leapyear(8) == "8 is a leap year"

        #second test
        assert leapyear.leapyear(3) == "3 is not a leap year"
        assert leapyear.leapyear(2001) == "2001 is not a leap year"
