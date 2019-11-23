# graph class representation
from graph_representations import graph

class Graph:
    def __init__(self, graph=None):
        if not graph:
            self.__graph = dict()
        else:
            self.__graph = graph

    @staticmethod
    def print_graph():
        print()
        

if __name__ == "__main__":
    graph_obj = Graph(graph)
    print(graph_obj)
        

