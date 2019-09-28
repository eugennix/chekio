def disconnected_users(net, users, source, crushes):
    # Nobody will get a mesage if node that sends 
    # emails is crushed
    if source in crushes:
        return sum(people for node, people in users.items())
        
    # all nodes in city    
    n1, n2 = zip(*net)
    nodes = set(n1 + n2)
    visited, bad = set(), set(crushes)
    
    # start visit other nodes
    next_step = [source]

    while next_step:
        node = next_step.pop()
        visited.add(node)
        # find linked nodes
        for link in net:
            # visit it if it was not visited
            # and not in crushed node
            if node == link[0] and \
                    link[1] not in (visited | bad):
                next_step.append(link[1])
            elif node == link[1] and \
                    link[0] not in (visited | bad):
                next_step.append(link[0])
    
    # sum of users in not visited nodes
    return sum(users[x] for x in nodes if x not in visited)
     

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')