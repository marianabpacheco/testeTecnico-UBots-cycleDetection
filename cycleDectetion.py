def has_cycle(currentNode, visited = [] ):
    print(currentNode)
    if(currentNode in visited):
        return 1
    else:
        visited.append(currentNode)
        if(currentNode.next == None):
            return 0;
        else:
            return has_cycle(currentNode.next,visited)