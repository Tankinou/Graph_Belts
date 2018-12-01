# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:33:29 2018

@author: tancr
"""
#%%
      "White Belt"
#Create a function non_connected to find non-connected nodes in a graph


graph = {
        "a":["b","c"],
        "b":["d"],
        "c":["d"],
        "d":[],
        "e":[]
}
lst=[]
def get_all_nodes(g):
    for i in g:
        lst.append(i)
    
    print(lst)
    
    
def get_all_edges(g):
    edges = []
    for i in g:
        
        for e in g[i]:
        
            edges.append(i +" -> "+ e)
        
    print(edges)

def get_all_non_connected(g):
    non_con = []
    
    for i in g:
        if g[i] == []:
                non_con.append(i)
                
    print(non_con)


#%%
    
    
#Create a function fully_connected to that returns True if a graph is fully connected, False otherwise




graph = {
        "a":["b","c"],
        "b":["d"],
        "c":["d"],
        "d":[],
        "e":[]        
}

graph1 = {
        "a":["b","c"],
        "b":["a","c"],
        "c":["a","b"],
}

graph2 = {
        "a":["b","c","d"],
        "b":["c", "d"],
        "c":[],
        "d":["d"]
}
lst=[]
def get_all_nodes(g):
    for i in g:
        lst.append(i)
    
    print(lst)
    
    
def get_all_edges(g):
    edges = []
    for i in g:
        
        for e in g[i]:
        
            edges.append(i +" -> "+ e)
        
    print(edges)

def get_all_non_connected(g):
    non_con = []
    for i in g:
        if g[i] == []:
                non_con.append(i)
                
    print(non_con)

def all_connected(g):
    nodes = list(g.keys())
    for i in g:
       
#        print(len(nodes))
#        print(len(g[i]))
        if len(g[i]) == len(nodes)-1:
            return True
            
        else:
            return False



def fully_connected (g):
    nodes = len(list(g.keys()))
    edges = []
    
    for node in g:
        for edge in g[node]:
            edges.append(edge)
    
    return len(edges) == nodes * (nodes - 1)



















