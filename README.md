# OSM Graph Route
This project uses Dijkstra's algorithm on Open Street Map data. The project consists of two classes. The `Graph` class provides a graph representation of the data via methods such as `add_node` to add a node the graph, `add_edge` to add an edge between two ndoes, and 'get_shortest_path' which applies 'Dijkstra's algorithm' to find the shortest path between two points. The `Parser` class parses the command line arguments in order to run the program with the shell script `run.sh`. 

## Requirements
* Python 2.7 - check using this command `python --version`

## Instructions
1. Checkout the github repo: `https://github.com/MaraimElbadri/osm_graph`.
2. Setup the dependencies:

```
cd osm_graph
chmod +x run.sh
```

## Execution
A shell script `run.sh` has been provided to execute the program. The script passes 3 arguements to the Python program in the following format `./run.sh <path to graph> <from-osm-id> <to-osm-id>`.

### Example
```
./run.sh citymapper-coding-test-graph.dat 316319897 316319936
121
```

## Check list 
- [x] construct a graph from the data 
- [x] parse the command line arguments 
- [x] Dijkstra's algorithm to find shortest path between two nodes




