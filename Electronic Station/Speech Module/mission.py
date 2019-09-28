FIRST_TEN = ['', "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
FIRST_20 = ['', "one", "two", "three", "four", "five", "six", "seven", "eight", 
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = " hundred"


def checkio(number):
    if (result := FIRST_TEN[number//100]):
        result += HUNDRED
    if (x := number%100):
        result += ' ' if result else ''
        if 0 < x < 20:
            result += FIRST_20[x]
        else:
            result += OTHER_TENS[x//10-2]
            if (x := x%10):
                result += ' ' + FIRST_TEN[x]
    return result
    
