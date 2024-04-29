Graph Data Structure Implementation in Python

Overview

This repository contains a comprehensive implementation of a Graph data structure in Python. The Graph class provides a robust and feature-rich structure for working with graphs, including methods for adding/removing vertices and edges, checking connectivity, getting neighbors, degree, total edges, and vertices.

Features

- Supports both directed and undirected graphs
- Implements essential graph operations:
    - Adding/removing vertices and edges
    - Checking connectivity between vertices
    - Getting neighbors, degree, total edges, and vertices
- Includes a clear and concise interface for working with graphs

Usage

1. Import the Graph class: from graph import Graph
2. Create a new graph instance: g = Graph()
3. Use the various methods to manipulate and query the graph

Methods

- add_Vertex(vertex): Adds a new vertex to the graph
- remove_Vertex(vertex): Removes a vertex from the graph
- add_Edge(source, destination): Adds a new edge between two vertices
- remove_Edge(source, destination): Removes an edge between two vertices
- is_Connected(source, destination): Checks if two vertices are connected
- neighbors(vertex): Returns a list of neighboring vertices
- degree(vertex): Returns the degree of a vertex
- total_Edges(): Returns the total number of edges in the graph
- total_Vertices(): Returns the total number of vertices in the graph
- clear_Graph(): Clears the graph
- print_Graph(): Prints the graph's adjacency list

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author

[Saman Ahmad @CodeWithSalman]
