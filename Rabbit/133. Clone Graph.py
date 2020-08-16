
"""
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.val = x
        self.neighbors = []
"""

"""
algo:
- 這裡的關鍵就是, 由於build一個graph還要考慮要traverse什麼的，所以用一個hashmap去暫存答案，各點都用hashmap lookup
- queue的使用，因為是在traverse一個graph, 在某個點時，都無法知道所有要做的事，所以每看到一個就往TODO list裡加一個
- BFS特徵：curr的鄰居都在curr加到queue
https://github.com/qiyuangong/leetcode/blob/master/python/133_Clone_Graph.py
"""
def cloneGraph(self, node):
    # BFS
    if node is None:
        return None

    val_map = {}
    queue = [node]
    graphCopy = UndirectedGraphNode(node.val)
    val_map[node.val] = graphCopy
    while len(queue) > 0:
        curr = queue.pop(0)
        # 這裡就展現為何是BFS, 因為是遍歷鄰居
        for ne in curr.neighbors:
            if ne.val in val_map:
                val_map[curr.val].neighbors.append(val_map[ne.val])
            else:
                neighborCopy = UndirectedGraphNode(ne.val)
                val_map[curr.val].neighbors.append(neighborCopy)
                val_map[ne.val] = neighborCopy
                # queue用來存在此點看到的鄰居
                queue.append(ne)
    return graphCopy



# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

"""
自解recursion
- 就不用queue了
- BFS特徵：for loop中去rec
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        D = {}
        if not node:
            return node
        else:
            return self.rec(node, D)

    def rec(self, node, d):

        # 只有自己會把自己的clone加到hash map. 這很重要，因為hash map是當TODO list for traversal, 所以只在curr時加入
        curr = Node(val=node.val)
        d[node.val] = curr

        for ne in node.neighbors:

            if ne.val in d:

                d[node.val].neighbors.append(d[ne.val])
            else:
                # hey neighbor, 還沒看到你, 先去把你自己加進hash map裡
                tmp = self.rec(ne, d)
                d[node.val].neighbors.append(tmp)

        return curr


"""
其他兩個answer
"""

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






