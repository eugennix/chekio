def subnet_links(net, users, crushes):
    ''' count all possible links in crushed subnets 
        ==  sum(users**2) for normal subnets
          + sum(users) for crushed nodes
    '''
    # all nodes in city    
    n1, n2 = zip(*net)
    nodes_to_link = set(n1 + n2)
    crushed_nodes = set(crushes)
    subnets_users = []
    
    # DON't COUNT CRASHED SERVERS as subnet
    # remove crushed nodes
    nodes_to_link -= crushed_nodes
    
    # remove links to crushed nodes:
    crushed_net = [link for link in net
                    if link[0] not in crushed_nodes 
                    and link[1] not in crushed_nodes]

    # make subnets from not yet linkes nodes
    while nodes_to_link:
        # count people in next subnet
        subnet_count_user = 0
        # any node, not linked yet
        next_step = [nodes_to_link.pop()]

        while next_step:
            node = next_step.pop()
            subnet_count_user += users[node]
    
            # find linked nodes in CRUSHED_NET
            for link in crushed_net:
                if node == link[0] \
                    and link[1] in nodes_to_link:
                        next_step.append(link[1])
                        nodes_to_link.remove(link[1])
                elif node == link[1] \
                    and link[0] in nodes_to_link:
                        next_step.append(link[0])
                        nodes_to_link.remove(link[0])
        # total users in this subnet counted
        subnets_users.append(subnet_count_user)
        
    return sum(u**2 for u in subnets_users) +\
           sum(users[n] for n in crushes)
    

def most_crucial(net, users):
    crush_results = []
    # try to crush every nodes by one, store results
    for crush in users.keys():
        crush_results.append([subnet_links(net, users, crush), crush])

    crush_results.sort()
    min_result = crush_results[0][0]
    
    return [x[1] for x in crush_results if x[0] == min_result]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')