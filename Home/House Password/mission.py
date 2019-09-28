def checkio(data: str) -> bool:

    if len(data) < 10:
        # lenght too short
        return False
        
    if data == data.upper():
        # data not changed  -> no lowercase in data
        return False
    
    if data == data.lower():
        # data not changed  -> no uppercase in data
        return False
    
    for digit in '0123456789':
        if data.find(digit) != -1:
            # found at least 1 digit
            return True
            
    # digits not found
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
