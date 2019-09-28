def checkio(numbers):
    # dynamic programming
    
    # f[0] - start platform, f[-1] - finish platform
    f = [0]*(len(numbers)+2)
    
    # add 2 zero cells for usability, so f[1] process in cycle
    cost = [0] + numbers + [0]
    
    for step in range(1, len(f)):
        f[step] = max(f[step-1], f[step-2]) + cost[step]

    return f[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')