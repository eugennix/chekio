from typing import List
from collections import deque

def checkio(land_map: List[List[int]]) -> List[int]:
    max_I, max_J = len(land_map), len(land_map[0])
    islands_sizes = []

    process_deque = deque()
    for i in range(max_I):
        for j in range(max_J):
            if land_map[i][j]:
                # found new island
                process_deque.append((i, j))
                land_map[i][j] = 0
                size_of_island = 0
                while process_deque:
                    node_i, node_j = process_deque.popleft()
                    size_of_island += 1
                    for ix in range(node_i-1, node_i+2):
                        if 0 <= ix < max_I:
                            for jx in range(node_j-1, node_j+2):
                                if (0 <= jx < max_J) and land_map[ix][jx]:
                                    process_deque.append((ix, jx))
                                    land_map[ix][jx] = 0
                islands_sizes.append(size_of_island)

    return sorted(islands_sizes)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")