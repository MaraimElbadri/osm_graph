# OSM Graph Route
This project uses Dijkstra's algorithm on Open Street Map data. The project consists of two classes. The `Graph` class provides a graph representation of the data via methods such as `add_node` to add node the graph, `add_edge` to add edge to the graph and 'get_shortest_pah' which applies 'Dijkstra's algorithm' to find the shortest path between two points. The 'Parser' class parses the command line arguments in order to run the program with the shell script `run.sh`. 

## Requirements
* Python 2.7 - check using this command `python --version`

## Instructions
1. Checkout the repo from github `https://github.com/MaraimElbadri/osm_graph` 
2. Setup the dependencies:
`
$ cd osm_graph
$ export PYTHONPATH=$PYTHONPATH:$(pwd)
$ chmod +x run.sh
`

## Execution
A simple shell script run.sh has been provided to execute the program. This passes 3 arguements to the Python application `./run.sh <path to graph> <from-osm-id> <to-osm-id>`.

### Example
`./run.sh citymapper-coding-test-graph.dat 316319897 316319936
121`

## Check list 
- [x] construct a graph from the data 
- [x] parse the command line arguments 
- [x] Dijkstra's algorithm to find shortest path between two nodes




