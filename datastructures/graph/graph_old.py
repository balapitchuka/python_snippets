from collections import defaultdict

graph = defaultdict(list)
def addedge(graph, src_node, dest_node):
    graph[src_node].append(dest_node)

def generate_edge_list(graph):
    edge_list = list()
    for node in graph:
        for node_neibr in graph[node]:
            edge_list.append((node, node_neibr))
    return edge_list



addedge(graph,'a','c') 
addedge(graph,'b','c') 
addedge(graph,'b','e') 
addedge(graph,'c','d') 
addedge(graph,'c','e') 
addedge(graph,'c','a') 
addedge(graph,'c','b') 
addedge(graph,'e','b') 
addedge(graph,'d','c') 
addedge(graph,'e','c')

print(generate_edge_list(graph))

