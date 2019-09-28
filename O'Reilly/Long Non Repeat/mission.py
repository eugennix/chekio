def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    # brute force :-(
    if len(line):
        # try different lengths, begin from max
        for max_len in range(len(line), 0, -1):
            
            # try substrings from begin of line
            for left in range(0, len(line) - max_len + 1):
                if is_uniq(line[left : left + max_len]):
                    # found
                    return line[left : left + max_len]
    # empty line
    return ''

def is_uniq(line: str) -> bool:
    """ is all symbols differ each other """
    for x in line:
        if line.count(x) > 1:
            return False
    return True
    
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')