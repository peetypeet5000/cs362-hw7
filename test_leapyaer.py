import pytest
import leapyear

class TestLeapyear:
    def test(self):
        assert leapyear.leapyear(4) == "4 is a leap year"
        assert leapyear.leapyear(8) == "8 is a leap year"
