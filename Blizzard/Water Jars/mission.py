from collections import deque

def checkio(first_volume, second_volume, goal):
    # make BFS - start from two emply jars, try any actions
    # store previous status (j1, j2), 'action', number of steps to reach this
    # initial == ((None, None), None, too_big)

    # initialize by plus infinity ;-0 greater than number of cells in status table
    too_big = (first_volume+2)*(second_volume+2)
    # make universal solution, (limited of memory, ofcause)
    jars_status = [[((None, None), None, too_big)]*(second_volume+1) 
                    for _ in range(first_volume+1)]
    
    # get actions from testing system ;-), thanks a lot
    actions = {
            "01": lambda f, s: (first_volume, s),
            "02": lambda f, s: (f, second_volume),
            "12": lambda f, s: (f-(second_volume-s if f>second_volume-s else f),
                second_volume if f > second_volume - s else s + f),
            "21": lambda f, s: (first_volume if s > first_volume-f else s+f,
                s - (first_volume-f if s > first_volume-f else s), ),
            "10": lambda f, s: (0, s),
            "20": lambda f, s: (f, 0) }
        
    # start with empty jars
    jars_status[0][0] = ((0, 0), '00', 0)
    to_do = deque()
    to_do.append((0, 0))
    solution = []
    
    # BFS, key == number of steps to reach status
    while to_do:
        j1_x, j2_x = to_do.popleft()
        if j1_x == goal or j2_x == goal:
            # found goal in jar1 or jar2, restore solution
            while jars_status[j1_x][j2_x][2]:
                solution.append(jars_status[j1_x][j2_x][1])
                j1_x, j2_x = jars_status[j1_x][j2_x][0]
            # reverse actions
            solution = solution[::-1]
            break

        step_count = jars_status[j1_x][j2_x][2] + 1
        # try any possible actions
        for act in actions:
            j1, j2 = actions[act](j1_x, j2_x)
            if j1 or j2:
                if jars_status[j1][j2][2] > step_count:
                    jars_status[j1][j2] = ((j1_x,j2_x), act, step_count)
                    to_do.append((j1, j2))
    return solution

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, initial_data, max_steps):
        first_volume, second_volume, goal = initial_data
        actions = {
            "01": lambda f, s: (first_volume, s),
            "02": lambda f, s: (f, second_volume),
            "12": lambda f, s: (
                f - (second_volume - s if f > second_volume - s else f),
                second_volume if f > second_volume - s else s + f),
            "21": lambda f, s: (
                first_volume if s > first_volume - f else s + f,
                s - (first_volume - f if s > first_volume - f else s),
            ),
            "10": lambda f, s: (0, s),
            "20": lambda f, s: (f, 0)
        }
        first, second = 0, 0
        result = func(*initial_data)
        if len(result) > max_steps:
            print("You answer contains too many steps. It can be shorter.")
            return False
        for act in result:
            if act not in actions.keys():
                print("I don't know this action {0}".format(act))
                return False
            first, second = actions[act](first, second)
        if goal == first or goal == second:
            return True
        print("You did not reach the goal.")
        return False

    assert check_solution(checkio, (5, 7, 6), 10), "Example"
    assert check_solution(checkio, (3, 4, 1), 2), "One and two"
    
    # !!! some tests have jar volume == 10 
    checkio(8, 10, 4)
    
