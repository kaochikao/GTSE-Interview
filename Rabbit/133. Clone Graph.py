
def cloneGraph(self, start):
    if start==None: 
        return start
    clone = {} #[0]
    stack = [] #[1]
    
    clone[start] = Node(start.val, [])
    stack.append(start)
    
    while stack:
        node = stack.pop()
        for nb in node.neighbors:
            if nb not in clone: #[3]
                clone[nb] = Node(nb.val, [])
                stack.append(nb)
            clone[node].neighbors.append(clone[nb]) #[2]
            
    return clone[start]


def clone_graph(start):

    if not start:
        return start

    clone = {} # old_node : new_node
    stack = [] # 暫存, 以neighbor加入，pop出來就是node本身

    while stack:
        node = stack.pop()

        for nb in node.neighbors:
            if nb not in clone:
                clone[nb] = Node(nb.val, [])
                stack.append(nb)
            clone[node].neighbors.append(clone[nb])

    return clone[start]