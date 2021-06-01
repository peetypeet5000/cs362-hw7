#takes an integer year i and returns a string indicating if the year is a leap year or not
def leapyear(year):
    output = ""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                output = str(year) + " is a leap year"
            else:
                output = str(year) + " is not a leap year"
        else:
            output = str(year) + " is a leap year"
    else:
        output = str(year) + " is not a leap year"

    return output
    