
# coding: utf-8

# In[3]:

graph = {'Ant': ['Bat', 'Cat','Hyena'],
             'Bat': ['Cat', 'Dog'],
             'Cat': ['Dog','Eel','Fish','Ant'],
             'Dog': ['Cat','Eel'],
             'Eel': ['Fish','Ant','Bat'],
             'Fish': [],
             'Hyena': ['Fish','Ant','Bat','Eel']}

def edges_of_graph(graph): #to generate a list of all edges in the graph
    edges = []
    for node in graph:
        for neighbour_node in graph[node]:
            edges.append((node, neighbour_node))

    return edges

def isolated_nodes(graph): #to generate a list of isolated nodes
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated+=node #how do I prevent the string from being split into charaters in the output list?
    return isolated

print("The list of edges in the graph:",edges_of_graph(graph))
print("The list of isolated nodes are:",isolated_nodes(graph))

def all_paths(graph, start, end, path=[]): #finding all paths between two entries
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpath1 = all_paths(graph, node, end, path)
                for newpath2 in newpath1:
                    paths.append(newpath2)
        return paths
       

all_paths(graph, 'Ant', 'Dog')

