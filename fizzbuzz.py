#takes an int i and returns the fizzbuzz output at that line
def fizzbuzz(i):
    output = ''
    if i % 3 == 0:
        output += 'Fizz'
    if i % 5 == 0:
        output += 'Buzz'
    if i % 5 != 0 and i % 3 != 0:
        output = int(i)
    
    return output
    