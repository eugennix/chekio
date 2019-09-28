def can_pass(matrix, first, second):
    
    max_line, max_row = len(matrix), len(matrix[0])
    path_key = matrix[first[0]][first[1]]

    path_cells, processed = [first], {first}
    while path_cells:
        
        # process next cell in path
        cell_line, cell_row = path_cells.pop()
        
        # test its 4 neigbours 
        for d_line, d_row in (-1, 0), (1, 0), (0, -1), (0, 1):
            
            if (0 <= (neig_line := cell_line + d_line) < max_line
            and 0 <= (neig_row := cell_row + d_row) < max_row
            and (neig_line, neig_row) not in processed
            and matrix[neig_line][neig_row] == path_key):

                # found next cell in path
                if (neig_line, neig_row) == second:
                    # path reach target cell
                    return True
                else:
                    # add new cell to path
                    path_cells.append((neig_line, neig_row))
                    processed.add((neig_line, neig_row))
    # can't reach target sell
    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
                    
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
