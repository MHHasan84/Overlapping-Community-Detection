import pandas as pd
import networkx as nx
import numpy as np

class ProteinGraph:
    def __init__(self):
        self.df1=pd.read_csv("./dataset/ogbn_proteins/raw/edge.csv.gz",nrows=None)
        self.df2=pd.read_csv("./dataset/ogbn_proteins/raw/node_species.csv.gz")
    
    def get_graph(self):
        G = nx.from_pandas_edgelist(self.df1, "1", "96401")
        return G
    
    def get_graph_of_species(self,species_id):
        edges_array = self.df1[['1', '96401']].to_numpy()
        species_array = self.df2[['3702']].to_numpy()
        
        species_dict={}

        for species in self.df2['3702'].unique():
            species_dict[species]=[]

        for edge in edges_array:
            
            protein1=edge[0]
            protein2=edge[1]
            
            species1=species_array[protein1-1][0]
            species2=species_array[protein2-1][0]
            
            if species1==species2:
                species_dict[species1].append(edge)
        
        G=nx.Graph()
        G.add_edges_from(species_dict[species_id])
        
        return G