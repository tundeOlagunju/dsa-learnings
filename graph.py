from collections import defaultdict, deque
# Adjacency list
class Graph:
    def __init__(self, graph=None, edges=None, directed=False) -> None:
        if graph == None:
            self.graph = defaultdict(set)
        else: self.graph = graph
        self.directed = directed
        self.add_edges(edges)
        
    
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
        print("start_vertex", start_vertex)
        path = path + [start_vertex]
        print(path)

        if start_vertex == end_vertex:
            return path
        if start_vertex not in self.graph:
            return None
 
        for neighbour in self.graph[start_vertex]:
            if neighbour not in path:
                new_path = self.find_path(neighbour, end_vertex, path)
                print("here")
                if new_path:
                    return new_path    
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        
        if path == None: 
            path = []
        print("start_vertex", start_vertex)    
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
                print("new_paths", new_paths)
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
        


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "f", "c"},
      "e" : {"c", "f"},
      "f" : set()
    }
  
# graph = Graph(g)
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

# A good question on adj matrix on Leetcode is FriendCircles
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
                    visited.add(neighbour)
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
            move_count, node_left_in_layer, nodes_in_next_layer = 0, 1, 0
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
        dist = [[0]*self.column for i in range(self.row)]
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
print(dist)

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
n = Node(0)
print(n.neighbors)