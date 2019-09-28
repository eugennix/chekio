def make_cycle(path_start, teleports_map, cells_to_visit):
    destination = path_start[0]
    current_cell = path_start[-1]
    visited = len(set(path_start))

    for tele in teleports_map:
        if current_cell in tele:
            next_cell = tele[1] if current_cell == tele[0] else tele[0]
            path_start.append(next_cell)
            if next_cell == destination and visited == cells_to_visit:
                print('FOUND cycle', path_start)
                return True
            else:
                # remove used teleport from teleports_map
                teleports_map.remove(tele)
                if make_cycle(path_start, teleports_map, cells_to_visit):
                    # yet found cycle, don't process any more
                    return True
                else:
                    # remove cell from path and restore teleports_map
                    path_start.pop()
                    teleports_map.add(tele)
    return False


def checkio(teleports_string):
    # return any route from 1 to 1 over all points
    teleports_map = set([tuple(sorted([int(x), int(y)])) for x, y in
                     teleports_string.split(",")])
    cells = set()
    for c1, c2 in teleports_map:
        cells.add(c1)
        cells.add(c2)
    all_cells_in_cycle = len(cells)
    start_cell = 1
    path = [start_cell]

    make_cycle(path, teleports_map, all_cells_in_cycle)

    return ''.join([str(cell) for cell in path])


#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"