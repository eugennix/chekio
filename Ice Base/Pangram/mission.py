def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    text_letters = set(text.lower())
    a_to_z_pangram =  set('abcdefghijklmnopqrstuvwxyz')
    
    # a_to_z_pangram    is subset of    text_letters    or equal it
    return a_to_z_pangram <= text_letters

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
    print(check_pangram("abcdefghijklmnopqrstuvwxyz"))