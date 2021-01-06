import heapq
import sys
import json

import GraphInterface
from DiGraph import DiGraph
from DiGraph import Edge
from DiGraph import Node
from GraphInterface import GraphInteface

from GraphAlgoInterface import GraphAlgoInterface
from typing import List
import matplotlib.pyplot as plt
import numpy as np


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self, graph):
        self.dw_graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.dw_graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        new_nodes = {}
        new_edgesIn = {}
        new_edgesOut = {}
        try:
            with open(file_name, "r") as f:
                dict_graph = json.load(f)
                for k in dict_graph["Nodes"]:
                    position = k["pos"]
                    id = k["id"]
                    node = Node(int(id), sys.maxsize, 0, -1)

                    self.vehicles = new_vehicle_dict
            return True

        except IOError as e:
            print(e)
        return False

    def bfs(self, start_node: int, flag: bool) -> bool:
        """
        Performs breathd first search on the graph.
        """
        for n in self.dw_graph.get_all_v().values():
            n.visited = False
        queue = [self.dw_graph.nodes[start_node]]
        self.dw_graph.nodes[start_node].visited=True

        node_list=[start_node]
        while queue:
            current = queue.pop()
            if not flag:
                for e in self.dw_graph.all_out_edges_of_node(current.node_id).values():
                    if not self.dw_graph.nodes[e.dest].visited :
                        self.dw_graph.nodes[e.dest].visited=True
                        queue.append(self.dw_graph.nodes[e.dest])
                        node_list.append(e.dest)
            else:
                for e in self.dw_graph.all_in_edges_of_node(current.node_id).values():
                    if not self.dw_graph.nodes[e.src].visited :
                        self.dw_graph.nodes[e.src].visited=True
                        queue.append(self.dw_graph.nodes[e.src])
                        node_list.append(e.src)

        return node_list

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        try:
            graph = json.dumps(self.dw_graph, default, indent=4)
            f = open(file_name, "w")
            f.write(vehicles_json)
            f.close()
            return True

        except Exception as e:
            print(e)
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list

        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        if id1 == id2:
            return 0, [id1]

        for n in self.dw_graph.get_all_v().values():  # Set all distance to be max value.
            if n.node_id != id1:
                n.distance = sys.maxsize
                n.visited = 0
        path = []
        self.dw_graph.nodes[id1].distance = 0
        min_heap = [(n.distance, n) for n in
                    self.dw_graph.get_all_v().values()]  # Create ordered pairs in the min heap.
        heapq.heapify(min_heap)  # heapify to maintain the minimum

        while len(min_heap):
            node = heapq.heappop(min_heap)  # pop the smallest item
            current = node[1]  # Get node from tuples
            current.visited = 1  # Set the node to visited

            for neighbour in self.dw_graph.all_out_edges_of_node(current.node_id).values():  # Get neighbours
                if self.dw_graph.nodes[neighbour.dest].visited == 0:  # if we didn't visit this neighbour
                    new_dist = current.distance + neighbour.weight  # Set new distance

                    if self.dw_graph.nodes[
                        neighbour.dest].distance > new_dist:  # If new distance is smaller , update it.
                        self.dw_graph.nodes[neighbour.dest].distance = new_dist
                        min_heap.append((self.dw_graph.nodes[neighbour.dest].distance,
                                         self.dw_graph.nodes[neighbour.dest]))  # add to priority queue
                        heapq.heapify(min_heap)  # Heapify min.
                        self.dw_graph.nodes[neighbour.dest].parent = current.node_id  # Update parent

        if self.dw_graph.nodes[id2].distance == sys.maxsize:  # if the distance is still max value , can't reach
            return -1, []

        path.append(id2)
        current = self.dw_graph.nodes[id2].parent

        while current != -1:  # Traverse backwards until parent is -1
            path.append(current)
            current = self.dw_graph.nodes[current].parent
        path.reverse()
        return self.dw_graph.nodes[id2].distance, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        list1=self.bfs(id1,False)
        list2=self.bfs(id1,True)
        return list(set(list1) & set(list2))



    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        counter=0
        mega_list=[]
        for n in self.dw_graph.get_all_v().values():
            print("key is" ,n.node_id)
            if counter < self.dw_graph.v_size():
                counter=counter+len(self.connected_component(n.node_id))
                mega_list.append(self.connected_component(n.node_id))

        return mega_list

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        x_vals = [1, 2, 3, 4]
        y_vals = [1, 4, 9, 16]
        plt.plot(x_vals, y_vals, label="My first plot :)")
        plt.xlabel("x axis ")
        plt.ylabel("y axis ")
        plt.title("The title of the graph")
        plt.legend()
        plt.show()
