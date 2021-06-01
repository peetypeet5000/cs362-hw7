import pytest
import fizzbuzz

class TestFizzbuzz:
    def test(self):
        for i in [3, 6, 9, 12]:
            assert fizzbuzz.fizzbuzz(i) == "Fizz"
        for i in [5, 10, 15, 20]:
            assert fizzbuzz.fizzbuzz(i) == "Buzz"
