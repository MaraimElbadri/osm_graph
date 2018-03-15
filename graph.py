# class to construct a graph representation using adjacency list
class Graph:
    def __init__(self):
        graph_dictionary = {}
        self._graph_dictionary = graph_dictionary

    @property
    def graph_dictionary(self):
        return self._graph_dictionary


    def add_node(self, node):
        '''
        add a new node to the graph
        param node: a new node
        pre_conidtion: the node does not already exist 
        '''
        if node not in self._graph_dictionary:
            self._graph_dictionary[node] = {}

    @property
    def nodes(self):
        # return all nodes in the graph
        return list(self._graph_dictionary.keys())


    def add_edge(self, edge):
        """
        add a new edge to the graph
        :param edge: an edge connecting two nodes
        :param directional: boolean flag indicating edge to be direction to bidirectional
        """
        (node1, node2, dist) = tuple(edge)
        self.add_directional_edge(node1, node2, dist)

        #if not directional:
        #self.add_directional_edge(node2, node1, dist)

    def add_directional_edge(self, source, dest, dist):
        """
        adds a directional edge to the graph
        :param source: start node
        :param dest: end node
        :param dist: weight of edge
        """
        if source in self._graph_dictionary:
            self._graph_dictionary[source][dest] = int(dist)
        else:
            self._graph_dictionary[source] = {dest: int(dist)}

    def get_shortest_path(self, start, end):
        """
        calculate the shortest path for a weighted graph.
        param start: start node
        param end: end node
        return: an integer represents the length of the path between two distancews 
        """

        nodes_to_visit = {start}
        visited_nodes = set()

        dist_from_start = {}
        dist_from_start[start] = 0
        parents_list = {}

        while len(nodes_to_visit) < len(self._graph_dictionary):

            # The next node should be the one with the smallest weight
            # find the smallest weight from teh starting node and save the node at current_node
            min_distance = min([(dist_from_start[node], node) for node in nodes_to_visit])
            current_node= min_distance[1]

            if current_node == end:
                break

            # lock down the node with the smallest edge weight
            nodes_to_visit.remove(current_node)
            visited_nodes.add(current_node)

            # get the list of edges connect the current node and only safe the ones that have been visited 
            edges = self._graph_dictionary[current_node]
            unvisited_neighbours = set(edges).difference(visited_nodes)

            # loop through all set of neighbours
            for neighbour in unvisited_neighbours:
                neighbour_dist = dist_from_start[current_node] + edges[neighbour]

                # if the neighbour_dist is less than the best known distance to end_node, update the distance
                if neighbour_dist < dist_from_start.get(neighbour, float('inf')):
                    dist_from_start[neighbour] = neighbour_dist
                    parents_list[neighbour] = current_node
                    nodes_to_visit.add(neighbour)

        return dist_from_start[end]