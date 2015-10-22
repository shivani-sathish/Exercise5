
# coding: utf-8

# In[10]:

graph = {'Ant': ['Bat', 'Cat','Hyena'],
             'Bat': ['Cat', 'Dog'],
             'Cat': ['Dog','Eel','Fish','Ant'],
             'Dog': ['Cat','Eel'],
             'Eel': ['Fish','Ant','Bat'],
             'Fish': [],
             'Hyena': ['Fish','Ant','Bat','Eel']}

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
       

find_all_paths(graph, 'Ant', 'Dog')

