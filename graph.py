from collections import defaultdict, deque, Counter
# Adjacency list
class Graph:
    def __init__(self, graph=None, edges=None, directed=False) -> None:
        if graph == None:
            self.graph = defaultdict(set)
        else: self.graph = graph
        self.directed = directed
        # self.add_edges(edges)
        
    
    def add_edges(self, edges):
        if edges:
            for vertexA, vertexB in edges:
                self.add_edge(vertexA, vertexB)

    def edges(self, vertex):
        return self.graph[vertex]
    
    def all_vertices(self):
        return self.graph.keys()
    
    # edges == connections
    def all_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {vertex, neighbour} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    # not necessary for a default dict -> empty set anyway
    def add_vertex(self, vertex):
        pass
    
    # an edge is just a connection e.g ('A', 'B') means A -> B or B -> A for undirected 
    def add_edge(self, vertexA, vertexB):
        self.graph[vertexA].add(vertexB)
        if not self.directed:   
            self.graph[vertexB].add(vertexA)

    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None: 
            path = []
        # print("start_vertex", start_vertex)
        # path = path + [start_vertex]
        # print(path)
        path.append(start_vertex)
        # print(path)

        if start_vertex == end_vertex:
            return path
        if start_vertex not in self.graph:
            return None
 
        for neighbour in self.graph[start_vertex]:
            if neighbour not in path:
                new_path = self.find_path(neighbour, end_vertex, path)
                if new_path:
                    return new_path 
        path.pop()   
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        
        if path == None: 
            path = []
        # print("start_vertex", start_vertex)    
        #path.append(start_vertex) will never work because recursion at lower level modifies the path at higher level https://stackoverflow.com/questions/64403575/python-different-recursive-result-if-append-to-list-or-add-to-the-list
        path  = path + [start_vertex] 
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return None
        
        all_paths = []
        for neighbour in self.graph[start_vertex]:
            if neighbour not in path:
                new_paths = self.find_all_paths(neighbour, end_vertex, path)
                # print("new_paths", new_paths)
                for p in new_paths:
                    all_paths.append(p)
                    print("all_paths", all_paths)

        return all_paths

    def remove(self, vertex):
        if not self.graph[vertex]:
            return "Not present"
        else: del self.graph[vertex]

        for vertices in self.graph.values():
            if vertex in vertices:
                vertices.remove(vertex)
    
    def depth_first_search_r(self, start):
        visited = set()

        def dfs(node):
            visited.add(node)
            print(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        dfs(start)

    def depth_first_search_i(self, start):
        stack = [start]
        visited = set()

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                stack.extend(self.graph[node] - visited)

    # Friend circles leetcode
    def number_of_connected_components(self, n):
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        def findComponents():
            count = 0
            for i in range(n):
                if i not in visited:
                    count = count + 1
                    dfs(i)
            return count
                    
        return findComponents()


    def find_shortest_path(self, start_vertex, end_vertex):
        queue = deque()
        queue.append(start_vertex)
        visited = set()
        prev = {}

        def bfs():
            while queue:
                current = queue.popleft()
                visited.add(current)
                for neighbour in self.graph[current]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        prev[neighbour] = current
                        

        def reconstructPath():
            path = []
            def reconstruct(vertex):
                if vertex == start_vertex:
                    path.append(start_vertex)
                    return path
                path.append(vertex)
                return reconstruct(prev[vertex])
            return reconstruct(end_vertex)
 
        bfs()
        path = reconstructPath()
        return path[::-1]

    # topSort can only be applied on DAG
    # Kahn's Algorithm
    def topologicalSort(self, n):
        # get in degree of all the vertices
        in_degree = [0] * n
        for g in self.graph.values():
            for neighbour in g:
                in_degree[neighbour] += 1

        
        # enqueue nodes with no incoming edges first
        queue = deque(i for i, d in enumerate(in_degree) if d == 0)
        if len(queue) < 1: return None #i.e there is a cycle, there should be at least one node with in_degree 0
        topological_order = []
        while queue:
            curr = queue.popleft()
            topological_order.append(curr)
            if curr not in self.graph: continue
            for neigh in self.graph[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        # print(in_degree) at this point, sum(indegree) should be 0, or all values in in_degree should be 0
        if len(topological_order) != n: 
            return None #there is a cycle
        return topological_order

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b"},
      "d" : {"c", "a", "e"},
      "e" : {"d", "f"},
      "f" : {"e"}
    }

# directed acyclic graph
g2 = {2: {0, 4},
      0: {3, 1},
      4: {3, 5},
      3: {1},
      5: {1}
      }
  
# graph = Graph(g)
# print(graph.graph)
# print(graph.all_vertices())
# print(graph.all_edges())

# path = graph.find_path("a", "b", [])
# print(path)
# path = graph.find_path("a", "f")

# graph.depth_first_search_r("a")
# print(path)

# graph.remove("a")
# print(graph.graph)

# edges = [(0, 1), (1, 2), (3, 4)]
# graph2 = Graph(g)
# path = graph2.find_shortest_path('a', 'e')
# print(path)

graph2 = Graph(g2, directed=True)
graph2.topologicalSort(6)

# A good question on adj matrix on Leetcode is FriendCircles(Number of Provinces)
class Graph2:
    # adjacency matrix
    def __init__(self, vertex_num, edge_num) -> None:
        self.vertex_num = vertex_num
        self.edge_num = edge_num
        self.graph_mat = [[0 for i in range(vertex_num)] 
                        for j in range(vertex_num)]
    
    def addEdge(self, edge):
        start, end =  edge
        self.graph_mat[start][end] = 1
        self.graph_mat[end][start] = 1
    
    def bfs(self, start):
        visited = set()
        queue = deque()
        queue.append(start)
        while queue:
            current = queue.popleft()
            print(current, end = ' ')
            visited.add(current)
            for neighbour in range(self.vertex_num):
                if neighbour not in visited and self.graph_mat[current][neighbour] == 1:
                    visited.add(neighbour) #its actually important to visit here for bfs
                    queue.append(neighbour)
    
    def dfs(self, start):
        visited = set() #this should be global or pass it around 
        def do_dfs(start):
            print(start, end = ' ')
            visited.add(start)
            for i in range(len(self.graph_mat[start])):
                if i not in visited and self.graph_mat[start][i] == 1:
                    do_dfs(i)
    
        do_dfs(start)

v, e = 5, 4
# Create the graph
G = Graph2(v, e)
G.addEdge((0, 1))
G.addEdge((0, 2))
G.addEdge((0, 3))
G.addEdge((0, 4))
# G.dfs(0)
# G.bfs(1)



#Let's talk grids -- We can also DFS and BFS on grids. A perfect example is Number Of Islands on Leetcode


class Grid:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.row = len(self.grid) 
        self.column = len(self.grid[0])

    def dfs(self):
        pass

    #Assume in this case, the grid is unweighted and cells connect L,R,U,D
    #number of moves from start to end using BFS or distance b/w the two cells 'S' and 'E'
    #Another way to do this is to compute the distance array 
    def quickest_way_out(self):
        row_direction = [-1, +1, 0, 0]
        column_direction = [0, 0, +1, -1]
        row_queue, col_queue = deque(), deque()
        start_row, start_column  = 0, 0
        visited = set()

        def explore_neighbours(row, col, nodes_in_next_layer):

            def is_valid(row_neighbour, col_neighbour):
                if (row_neighbour < 0 or col_neighbour < 0 or row_neighbour >= self.row or col_neighbour >= self.column or self.grid[row_neighbour][col_neighbour] == '#' or (row_neighbour, col_neighbour) in visited):
                    return False
                return True
                    

            for i in range(4):
                row_neighbour = row + row_direction[i]
                col_neighbour = col + column_direction[i]
                if is_valid(row_neighbour, col_neighbour):
                    row_queue.append(row_neighbour)
                    col_queue.append(col_neighbour)
                    visited.add((row_neighbour, col_neighbour))
                    nodes_in_next_layer += 1
            return nodes_in_next_layer


        def bfs():
            move_count, node_left_in_layer, nodes_in_next_layer = 0, 1, 0 #variables to track the number of steps taken
            reached_end = False
            row_queue.append(start_row)
            col_queue.append(start_column)
            
            while row_queue: 
                row = row_queue.popleft()
                col = col_queue.popleft()
                
                visited.add((row, col))
             
                if self.grid[row][col] == 'E':
                    reached_end = True
                    break

                nodes_in_next_layer = explore_neighbours(row, col, nodes_in_next_layer)
                node_left_in_layer -= 1
                
                if node_left_in_layer == 0:
                    node_left_in_layer = nodes_in_next_layer
                    nodes_in_next_layer = 0
                    move_count += 1

            if reached_end:
                return move_count
            return -1

        return bfs()   

    #distance array for other cells from a cell 
    def distance_array(self, start):
        visited = set()
        queue = deque()
        dist = [[0] * self.column for i in range(self.row)]
        row_direction = [-1, +1, 0, 0]
        column_direction = [0, 0, +1, -1]
        queue.append(start)

        while queue:
            curr = queue.popleft()
            visited.add(curr)
            #explore neighbours
            for i in range(4):
                row_neigh = curr[0] + row_direction[i]
                col_neigh = curr[1] + column_direction[i]
                if row_neigh >= 0 and col_neigh >= 0 and row_neigh < self.row and col_neigh < self.column and (row_neigh, col_neigh) not in visited:
                    queue.append((row_neigh, col_neigh))
                    dist[row_neigh][col_neigh] = dist[curr[0]][curr[1]] + 1
        
        return dist


#From William Fiset's video on YT. Quickest path from start to end
dungeon = [
        ['S', '.', '.', '#', '.', '.', '.'], 
        ['.', '#', '.', '.', '.', '#', '.'], 
        ['.', '#', '.', '.', '.', '.', '.'], 
        ['.', '.', '#', '#', '.', '.', '.'], 
        ['#', '.', '#', 'E', '.', '#', '.']
        ]

gr = Grid(dungeon)
num_of_moves = gr.quickest_way_out()
# print(num_of_moves)

grid = [
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ]

gr2 = Grid(grid)
dist = gr2.distance_array((0,0))
# print(dist)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
n = Node(0)
# print(n.neighbors)

#Union Find algorithm can be improved by path with compression and union by rank/size (dont confuse with height)
#Union Find by size (or weighted quick union) is log N for union and log N for connected snce we are keeping the tree balanced. although O(N) for the constructor
#When using the combination of union by rank and the path compression optimization, the find operation will take O(α(N)) time on average. Since union and connected both make calls to find and all other operations require constant time, union and connected functions will also take O(α(N)) time on average.
#N is the number of vertices in the graph. α refers to the Inverse Ackermann function. In practice, we assume it's a constant. In other words, O(α(N)) is regarded as O(1) on average.
class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    #find the root of a particular node and compress path
    #path compression improves the time complexity of any node to constant time!!
    def root(self, i):
        while self.parent[i] != i:
            #self.parent[i] = self.parent[self.parent[i]] #make every other node in path points to its grandparent (path compression)
            i = self.parent[i]
        return i
        

    #notice that to find the root node, we need to traverse the parent nodes sequentially until we reach the root node. If we search the root node of the same element again, we repeat the same operations. Is there any way to optimize this process?
   #The answer is yes! After finding the root node, we can update the parent node of all traversed elements to their root node. When we search for the root node of the same element again, we only need to traverse two elements to find its root node, which is highly efficien
    def root2(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.root2(self.parent[x])
        return self.parent[x]

    # optimization: union by size, always attach the root of smaller tree to the root of larger one (in terms of size i.e number of nodes). Keeps the tree
    # balanced thereby improving the time complexity of depth of any node to logN
    def union(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)

        if rootP == rootQ: return #already connected or in the same component

        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else: 
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]

    #is p and q connected directly/indirectly
    # connection is transitive (if p is connected to q and q is connected to r then p is connected to r)
    # symmetric (if p is connected to q then q is connected to p)
    # reflexive(p is connected to itself)
    def connected(self, p, q):
        return self.root(p) == self.root(q)


"""
Given an int n. You can use only 2 operations:
- multiply by 2
- integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.

Example 1:

Input: 10
Output: 6
Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
6 steps required, as we have used 5 multiplications by 2, and one division by 3.
Example 2:

Input: 3
Output: 7
Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.

Follow up: Use BFS
"""

def min_steps(num):

    def dfs(start, level):
        if start == num:
            return level
        
        dfs(start * 2, level + 1)
        dfs(start // 3, level + 1)


    dfs(1, 0)

import collections

def min_steps_2(num):

    queue = collections.deque()
    queue.append(1)
    level = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            if curr == num:
                return level
            
            queue.append(curr * 2)
            queue.append(curr // 3)
        
        level += 1
    
    return level

print(min_steps_2(3))




# https://leetcode.com/discuss/interview-question/413734/Bloomberg-or-Re-order-Array-Based-on-Dictionary

def reOrderArray(employees, order):
    graph = defaultdict(list)
    in_degree = Counter()



            
            
employees = [['John', 'Manager'], ['Sally', 'CTO'], ['Sam', 'CEO'], ['Drax', 'Engineer'], ['Bob', 'CFO'], ['Daniel', 'Engineer']]
order = {'CTO': 'CEO', 'Manager': 'CTO', 'Engineer' : 'Manager', 'CFO' : 'CEO'}
reOrderArray(employees, order)



"""
Remove ints from an array.

Example:

Input: array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
Output: [-8, 3, -5, 29, 43, 76, 73, 76]
Is there a corresponding or relative leetcode question?
"""






            

