from typing import List
def get_sq(code: str) -> set:
    result = set()
    for i in range(len(code)//2,):
        d1 = int(code[i*2], base=17)
        d2 = int(code[i*2+1], base=17)
        result.add((d1, d2))
    return result
        

def checkio(lines_list: List[List[int]]) -> int:
    """Return the quantity of squares"""
    # don't know how to solve
    possible = ('12261556', '23372667', '34483778',
                '56599A6A', '676A7BAB', '787BBC8C',
                '9D9ADEAE', 'ABAEEFBF', 'BCBFCGFG',
                '122315599AAB377B', '233426486AABBC8C',
                '5667599DDEEF7BBF', '67786A8CAEEFFGCG',
                '1223344815599DDEEFFG8CCG')
    result = 0
    # normalize d1 < d2 in link
    field = set([(min(x), max(x)) for x in lines_list])
    for sq_code in possible:
        sq = get_sq(sq_code)
        if len(sq - field) == 0:
            # print('found', sq_code)
            result += 1
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")