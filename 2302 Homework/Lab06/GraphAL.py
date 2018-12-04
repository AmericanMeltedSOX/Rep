"""
CS 2302: LAB 6 Option A
From: ISAAC ACOSTA
DATE: 12/04/18
"""

class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        self.dsf[a] = self.find(self.dsf[a])

        return self.dsf[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.dsf[rb] = ra

    def get_num_of_sets(self):
        count = 0

        for num in self.dsf:
            if num < 0:
                count += 1

        return count



class GraphALNode:
    def __init__(self, item, weight, next):
        self.item = item
        self.weight = weight
        self.next = next

# Edge node for kruskal's a;gorithm
class EdgeNode:
    def __init__(self, point_A, point_B, weight):
        self.point_A = point_A
        self.point_B = point_B
        self.weight = weight

    def print_edge(self):
        print("Point A:", self.point_A, "Point B:", self.point_B, "Weight:",self.weight)



class GraphAL:
    def __init__(self, initial_num_vertices, is_directed):
        self.adj_list = [None] * initial_num_vertices
        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_list)

    def add_vertex(self):
        self.adj_list.append(None)

        return len(self.adj_list) - 1  # Return new vertex id

    # Adds edge to graph
    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return  # If source and dest is not valid, returns none

        #  TODO: What if src already points to dest?
        self.adj_list[src] = GraphALNode(dest, weight, self.adj_list[src])

        # dest connects to source if not directed
        if not self.is_directed:
            self.adj_list[dest] = GraphALNode(src, weight, self.adj_list[dest])

    def remove_edge(self, src, dest):
        self.__remove_directed_edge(src, dest)

        if not self.is_directed:
            self.__remove_directed_edge(dest, src)

    def __remove_directed_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return  # Returns none if source or dest are not valid

        if self.adj_list[src] is None:
            return  # returns none if source does not direct to any other vertex

        if self.adj_list[src].item == dest: # Removes edge directed from dest
            self.adj_list[src] = self.adj_list[src].next
        else:
            prev = self.adj_list[src]
            cur = self.adj_list[src].next

            while cur is not None:
                if cur.item == dest:
                    prev.next = cur.next
                    return

                prev = prev.next
                cur = cur.next

        return len(self.adj_list)

    def get_num_vertices(self):
        return len(self.adj_list)

    # Gets verteces adjacent and directed from soource
    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.adj_list[src]

        while temp is not None: # Goes through adjacency list index to check fro verteces adjacent and directed from source
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item == dest:
                    vertices.add(i)
                    break

                temp = temp.next

        return vertices

    def get_edge_weight(self, src, dest):

        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        temp = self.adj_list[src]

        while temp is not None:
            if temp.item == dest:
                return temp.weight

            temp = temp.next

        return 0

    # ---------------------------------------------------------------------------------------
    def get_vertex_in_degree(self, v):
        if not self.is_valid_vertex(v):
            return  # Returns none if vertex is not valid

        in_degree_count = 0

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            # Checks for adjacent verteces
            while temp is not None:
                if temp.item == v:
                    in_degree_count += 1
                    break

                temp = temp.next

        # Returns number of indegrees
        return in_degree_count

    def get_sorted_edges(self):

        already_visited = []    # List of verteces already visited
        edge_list = []  # List of edges

        for i in range(len(self.adj_list)): # Goes through every index of the adjacency list
            temp = self.adj_list[i]

            while temp is not None:
                if temp.item not in already_visited:    # Checks if edge path has already been visited by checking verteces
                    edge_list.append(EdgeNode(i, temp.item, self.get_edge_weight(i, temp.item)))
                    # Adds Edge Attributes to edge list

                temp = temp.next
            # Vertex i is added to the visited verteces list
            already_visited.append(i)

        # Bubble sort of edge from least to greatest
        n = len(edge_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if edge_list[j].weight > edge_list[j+1].weight:
                    edge_list[j], edge_list[j+1] = edge_list[j+1], edge_list[j]

        # Returns edge list
        return edge_list

    def get_num_connected_components(self):

        dsf = DisjointSetForest(len(self.adj_list))

        for i in range(len(self.adj_list)):
            temp = self.adj_list[i]

            while temp is not None:
                dsf.union(i, temp.item)

                temp = temp.next

        return dsf.get_num_of_sets()

    #-----------------------------------------------------------------------
    def compute_indegree_every_vertex(self):

        indegree_list = []  # List to store indegrees of every vertex

        # Computes indegree of every vertex
        for i in range(len(self.adj_list)):
            num = self.get_vertex_in_degree(i)
            indegree_list.append(num)

        return indegree_list
