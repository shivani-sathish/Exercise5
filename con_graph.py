
# coding: utf-8

# In[10]:

class Random_graph:
    def __init__(self):
        self.nodes=[] 
        
    def add_node(self, node):
        self.nodes.append(node)
    
        return self.nodes

    def edges_of_graph(self): #to generate a list of all edges in the graph
        self.edges = []
        for node1 in self.nodes:
            for neighbour_node in self.nodes[node1]:
                self.edges.append((node1, neighbour_node))
        return self.edges

node_list=Random_graph()
node_list.add_node("Cat")
node_list.add_node("Mouse")
node_list.add_node("Deer")
node_list.add_node("rabbit")
node_list.add_node("crow")




        
    

