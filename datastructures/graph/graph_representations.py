# graph representations in python

# 1.adjacency list representation  using dictionary
# undirected graph
graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"],
          'f' : []
         }

print(graph)

# print edges list in graph (undirected)
edge_list = list()
for node in graph:
    for edge in graph[node]:
        edge_list.append((node, edge))
print(edge_list)

# isolated node list
isolated_nodes = list()
for node in graph:
    if not graph[node]:
        isolated_nodes.append(node)
print(isolated_nodes)

