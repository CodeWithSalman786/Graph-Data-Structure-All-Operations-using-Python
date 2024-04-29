#Author: @CodeWithSalman

# DECLARING A CLASS WITH THE NAME OF GRAPH.
class Graph:
    # NOW GOING TO USE CONSTRUCTOR.
    def __init__(self):
        # USE OF DICTIONARY.
        self.adj_List = {}
    # FUNCTION TO ADD VERTEX.
    def add_Vertex(self, vertex):
        if vertex not in self.adj_List:
            self.adj_List[vertex] = []
    # FUNCTION TO REMOVE VERTEX.
    def remove_Vertex(self, vertex):
        if vertex in self.adj_List:
            del self.adj_List[vertex]
        for neighbors in self.adj_List.values():
            if vertex in neighbors:
                neighbors.remove(vertex)
    # FUNCTION TO ADD EDGE.
    def add_Edge(self, source, destination):
        if source not in self.adj_List:
            self.add_Vertex(source)
        if destination not in self.adj_List:
            self.add_Vertex(destination)
        self.adj_List[source].append(destination)
        self.adj_List[destination].append(source)
    # FUNCTION TO REMOVE EDGE.
    def remove_Edge(self, source, destination):
        if source in self.adj_List and destination in self.adj_List[source]:
            self.adj_List[source].remove(destination)
            self.adj_List[destination].remove(source)
    # FUNCTION TO CHECK CONNECTIVITY.
    def is_Connected(self, source, destination):
        return destination in self.adj_List[source]
    # FUNCTION TO PRINT NEIGHBORS.
    def neighbors(self, vertex):
        if vertex in self.adj_List:
            return self.adj_List[vertex]
        else:
            return []
    # FUNCTION TO GET DEGREE OF VERTEX.
    def degree(self, vertex):
        if vertex in self.adj_List:
            return len(self.adj_List[vertex])
        else:
            return 0
    def total_Edges(self):
        total = 0
        for neighbors in self.adj_List:
            total += neighbors
        result = total // 2
        print("Total Edges are: ", result)
    def total_Vertices(self):
        return len(self.adj_List)
    def clear_Graph(self):
        return self.adj_List.clear()
    def print_Graph(self):
        for vertex, neighbors in self.adj_List.items():
            print(f"Vertex is {vertex} : and Neighbors are {neighbors}")
    def escape(self):
        exit()
if __name__ == '__main__':
    obj = Graph()
    while True:
        print("1 = ADD VERTEX")
        print("2 = REMOVE VERTEX")
        print("3 = ADD EDGE")
        print("4 = REMOVE EDGE")
        print("5 = CHECK CONNECTIVITY")
        print("6 = GET NEIGHBORS")
        print("7 = GET DEGREE")
        print("8 = TOTAL EDGES")
        print("9 = TOTAL VERTICES")
        print("10 = CLEAR GRAPH")
        print("11 = PRINT GRAPH")
        print("12 = EXIT OR ESCAPE")
        selection = int(input("Make any One Selection from Above: "))
        if selection == 1:
            value = int(input("Enter the Value for Node or Vertex: "))
            obj.add_Vertex(value)
        elif selection == 2:
            obj.print_Graph()
            value = int(input("Enter the Value for Node or Vertex: "))
            obj.remove_Vertex(value)
        elif selection == 3:
            source = int(input("Enter the Source: "))
            destination = int(input("Enter the Destination: "))
            obj.add_Edge(source, destination)
        elif selection == 4:
            obj.print_Graph()
            source = int(input("Enter the Source: "))
            destination = int(input("Enter the Destination: "))
            obj.remove_Edge(source, destination)
        elif selection == 5:
            obj.print_Graph()
            source = int(input("Enter the Source: "))
            destination = int(input("Enter the Destination: "))
            print(obj.is_Connected(source, destination))
        elif selection == 6:
            obj.print_Graph()
            neighbors = int(input("Enter the value of Vertex to get its Neighbors: "))
            result = obj.neighbors(neighbors)
            print("Total Neighbors are: ", result)
        elif selection == 7:
            obj.print_Graph()
            degree = int(input("Enter the Vertex Value to get its Degree: "))
            result = obj.degree(degree)
            print("The Degree is: ", result)
        elif selection == 8:
            obj.print_Graph()
            edges = int(input("Enter the Vertex Value to get its Connections: "))
            obj.total_Edges()
        elif selection == 9:
            vertices = int(input("Enter the Vertex Value to get Total Vertices or Nodes: "))
            obj.total_Vertices()
        elif selection == 10:
            obj.clear_Graph()
        elif selection == 11:
            obj.print_Graph()
        elif selection == 12:
            print("You Escaped Successfully.")
            exit(1)
        else:
            print("Selection out of Range.")
