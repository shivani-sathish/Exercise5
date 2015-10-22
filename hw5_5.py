
# coding: utf-8

# In[10]:

graph = {'Ant': ['Bat', 'Cat','Hyena'],
             'Bat': ['Cat', 'Dog'],
             'Cat': ['Dog','Eel','Fish','Ant'],
             'Dog': ['Cat','Eel'],
             'Eel': ['Fish','Ant','Bat'],
             'Fish': [],
             'Hyena': ['Fish','Ant','Bat','Eel']}

def shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath1 = find_shortest_path(graph, node, end, path)
                if newpath1:
                    if not shortest or len(newpath) < len(shortest): #to find shortest path
                        shortest = newpath1
        return shortest

print(find_shortest_path(graph, 'Hyena', 'Dog'))

