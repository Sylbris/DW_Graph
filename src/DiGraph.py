import GraphInterface



class DiGraph(GraphInterface):
    """This abstract class represents an interface of a graph."""
    def __init__(self):
        self.modeChanges = 0
        self.nodesOnGraph = 0
        self.edgesOnGraph = 0
        self.nodes = {int : Node}
        self.edgesIn = {int : {int : Edge}}
        self.edgesOut = {int : {int : Edge}}

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.nodesOnGraph

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edgesOnGraph

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph,
        each node is represented using a pair  (key, node_data)"""
        return  self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        return self.edgesIn.get['Type [int]':id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        return self.edgesOut.get['Type [int]':id1]

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        raise NotImplementedError

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id2 not in self.edgesOut.values():
            e = Edge(id1,id2,weight)
            self.edgesOut['Type [int]':id1]={id2,e}
            self.edgesIn['Type [int]':id2]={id1,e}
            self.edgesOnGraph = self.edgesOnGraph +1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.nodes.keys():
            n = Node(node_id,0.0,False)
            self.nodes['Type [int]':node_id] = n
            self.nodesOnGraph = self.nodesOnGraph +1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """

        "need to fix"
        if node_id in self.nodes:
            self.nodes.pop(node_id)
            self.nodesOnGraph = self.nodesOnGraph - 1

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id2 in self.edgesOut.get(node_id1).keys():
            self.edgesOut.get(node_id1).pop(node_id2)
            self.edgesOnGraph = self.edgesOnGraph -1
            return True
        return False

    """data structure to store graph edges"""
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


    """ data structure for adjacency list node"""
class Node:
    def __init__(self, node_id, total_weight, visited):
        self.node_id = node_id
        self.total_weight = total_weight
        self.visited = visited


