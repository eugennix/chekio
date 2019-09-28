def subnetworks(net, crushes):
    # all nodes in city    
    n1, n2 = zip(*net)
    nodes_to_link = set(n1 + n2)
    crushed_nodes = set(crushes)
    subnet_count = 0
    
    # ? why DON't COUNT CRASHED SERVERS as subnet ???
    # to pass tests crushed nodes removed
    nodes_to_link -= crushed_nodes
    
    # remove links to crushed nodes:
    crushed_net = [link for link in net
                    if link[0] not in crushed_nodes 
                    and link[1] not in crushed_nodes]

    # make subnets from not yet linkes nodes
    while nodes_to_link:
        subnet_count += 1
        # any node, not linked yet
        next_step = [nodes_to_link.pop()]

        while next_step:
            node = next_step.pop()

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
    return subnet_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')