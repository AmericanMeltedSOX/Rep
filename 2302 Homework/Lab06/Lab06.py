"""
CS 2302: LAB 6 Option A
From: ISAAC ACOSTA
DATE: 12/04/18
"""

from queue import Queue
from GraphAL import GraphAL

import time


def main():

        # Graph 1
      graph = GraphAL(initial_num_vertices=7, is_directed=True)
      #graph = GraphAM(initial_num_vertices=11, is_directed=True)

      graph.add_edge(0, 1)
      graph.add_edge(0, 4)

      graph.add_edge(1, 2)
      graph.add_edge(2, 3)
      graph.add_edge(3, 6)

      graph.add_edge(4, 5)
      graph.add_edge(4, 1)
      graph.add_edge(5, 6)
      graph.add_edge(5, 1)
      graph.add_edge(5, 3)


        # Graph 2
      graph_2 = GraphAL(4, False)

      graph_2.add_edge(0, 1, 6.0)
      graph_2.add_edge(0, 2, 1.0)
      graph_2.add_edge(0, 3, 3.0)

      graph_2.add_edge(1, 2, 5.0)
      graph_2.add_edge(1, 3, 4.0)

      graph_2.add_edge(2, 3, 2.0)

      start_time = time.time()

        # Prints topological sort
      order = graph_topological_sort(graph)
      print("Topoloical Sort: ", order)

      end_time = time.time()    # Running Time
      print("Topological Sort Running Time:", end_time - start_time)
      print()

      start_time = time.time()

        # Prints kruskal's algorithm
      order2 = graph_kruskals_alg(graph_2)
      print("Kruskal's Algorithm (Minimum Spanning Tree):")
      for i in range(len(order2)):
          order2[i].print_edge()

      end_time = time.time()    # Running time
      print("Kruskal's Algorithm Running Time:", end_time - start_time)


def graph_kruskals_alg(graph):

    # Sort edges by increasing cost
    e = graph.get_sorted_edges()
    T = []  # List containing minimal spanning tree
    cycle_list = [] # List containing visited verteces


    for i in range(len(e)):
        if e[i].point_A not in cycle_list:
            T.append(e[i])

        cycle_list.append(e[i].point_A) # Adds vertex to list to check for cycles in the following loops
    return T


def graph_topological_sort(graph):
    # Computes all indegrees
    all_in_degrees = graph.compute_indegree_every_vertex()
    sort_result = []

    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i) # enqueue

    while not q.empty():
        u = q.get() # dequeue
        sort_result.append(u)

        # Find adjacent verteces
        for reachable_vertices in graph.get_vertices_reachable_from(u):
            all_in_degrees[reachable_vertices] -= 1 # Removes adjacent verteces from list

            if all_in_degrees[reachable_vertices] == 0:
                q.put(reachable_vertices) # Adds to Queue

    if len(sort_result) != graph.get_num_vertices():
            return None

    return sort_result



main()
