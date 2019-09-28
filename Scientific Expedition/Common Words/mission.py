from collections import Counter

def checkio(first, second):
    w1 = set(first.split(','))
    w2 = set(second.split(','))
    result = ','.join(sorted(list(w1 & w2)))
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
