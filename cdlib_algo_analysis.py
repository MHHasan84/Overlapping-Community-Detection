import pandas as pd
import networkx as nx
from cdlib import algorithms
from cdlib import evaluation
from protein_graph import ProteinGraph

def run_algorithm(G):
    communities = algorithms.slpa(G,  t=21, r=0.1) #change algorithm name here
    return communities

def calculate_overlapping_modularity(G,communities):
    overlapping_modularity = evaluation.modularity_overlap(G, communities)
    print(overlapping_modularity)

def calculate_conductance(G,communities):
    conductance = evaluation.conductance(G,communities)
    print(conductance)

def calculate_modularity_density(G,communities):
    modularity_density = evaluation.modularity_density(G, communities)
    print(modularity_density)

def calculate_cut_ratio(G,communities):
    cut_ratio = evaluation.cut_ratio(G, communities)
    print(cut_ratio)

def main():
    pg=ProteinGraph()
    #To get graph for whole dataset
    G = pg.get_graph()
    #To get graph for particular species
    #G=pg.get_graph_of_species(3702)
    communities=run_algorithm(G)
    calculate_overlapping_modularity(G,communities)
    
if __name__=="__main__":
    main()