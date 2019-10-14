

class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = dict()
        self.__graph_dict = graph_dict
    

    def vertices_list(self):
        return list(self.__graph_dict.keys())
    
    def edge_list(self):
        return self.__generate_edges()
    
    def __generate_edges(self):
        edge_list = list()
        for node in self.__graph_dict:
            for node_neigh in self.__graph_dict[node]:
                edge_list.append((node, node_neigh))
        return edge_list
    
    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = list()
        

    
