import pytest
import fizzbuzz

class TestFizzbuzz:
    def test(self):
        for i in [3, 6, 9, 12]:
            assert fizzbuzz.fizzbuzz(i) == "Fizz"
        for i in [5, 10, 20]:
            assert fizzbuzz.fizzbuzz(i) == "Buzz"
        for i in [15, 30, 60]:
            assert fizzbuzz.fizzbuzz(i) == "FizzBuzz"
        for i in [1, 2, 4, 7, 61, 88]:
            assert fizzbuzz.fizzbuzz(i) == i
