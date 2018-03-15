from parser import Parser
from graph import Graph


# construct parser object and parse the command line arguments 
args = Parser().get_args()

# read the .dat file and construct the graph
with open(args.file_path, mode='r') as f:
    graph_obj = Graph()

    for line in f.read().splitlines():
        items = line.split()

        if len(items) == 3:
            graph_obj.add_node(items[0])
            graph_obj.add_node(items[1])
            graph_obj.add_edge(items)

# calculate the shortest distance between two nodes 
distance = graph_obj.get_shortest_path(args.start_node, args.end_node)
print(distance)
