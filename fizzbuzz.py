#takes an int i and returns the fizzbuzz output at that line
def fizzbuzz(i):
    if i % 3 == 0:
        return 'Fizz'
    if i % 5 == 0:
        return 'Buzz'