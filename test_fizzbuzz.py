import pytest
import fizzbuzz

class TestFizzbuzz:
    def test(self):
        #first test
        for i in [3, 6, 9, 12]:
            assert fizzbuzz.fizzbuzz(i) == "Fizz"

        #second test
        for i in [5, 10, 20]:
            assert fizzbuzz.fizzbuzz(i) == "Buzz"

        #third test
        for i in [15, 30, 60]:
            assert fizzbuzz.fizzbuzz(i) == "FizzBuzz"

        #fourth test
        for i in [1, 2, 4, 7, 61, 88]:
            assert fizzbuzz.fizzbuzz(i) == i
