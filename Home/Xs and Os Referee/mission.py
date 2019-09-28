from typing import List

def checkio(game_result: List[str]) -> str:
    g = game_result
    
    for i in range(3):
        if g[i][0] == g[i][1] == g[i][2] != '.':
            return g[i][0]
    
    for i in range(3):
        if g[0][i] == g[1][i] == g[2][i] != '.':
            return g[0][i]
    
    for a, b in [(0, 2), (2, 0)]:
        if g[0][a] == g[1][1] == g[2][b] != '.':
            return g[1][1]

    return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")