def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    result, count, prev = 0, 0, ''
    for s in line:
        if s == prev:
            count += 1
        else:
            prev = s
            count = 1
        result = max(result, count)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
