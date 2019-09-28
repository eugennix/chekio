VOWELS = "aeiouy"

def translate(phrase):
    pointer, result = 0, []
    while pointer < len(phrase):
        curr = phrase[pointer]
        result.append(curr)
        if curr == ' ':
            pointer += 1
        elif curr not in VOWELS:
            pointer += 2
        else:
            pointer += 3
    return ''.join(result)

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
