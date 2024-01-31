# Overlapping-Community-Detection
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="dataset-description">Dataset Description</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

There are many algorithms for detecting overlapping communities. But those algorithms were useful for small graphs. After analyzing most of the algorithms on our dataset, we found huge runtime or memory errors. We are using a large-scale weighted graph of protein-protein interaction as our dataset. We will try to find a useful method to detect overlapping communities of the proteins. 

<!-- DATASET DESCRIPTION -->
## Dataset Description

The `ogbn-proteins` dataset is an undirected, weighted, and typed (according to species) graph. Nodes represent proteins, and edges indicate different types of biologically meaningful associations between proteins, e.g., physical interactions, co-expression or homology [1,2]. All edges come with 8-dimensional features, where each dimension represents the approximate confidence of a single association type and takes values between 0 and 1 (the larger the value is, the more confident we are about the association). The proteins come from 8 species.


<!-- GETTING STARTED -->
## Getting Started

Follow these steps to run the code on your local machine.

### Prerequisites

* Python
* PyTorch
* PyTorch Geometric (PyG)
* OGB
* NetworkX
* CDLib

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MHHasan84/Overlapping-Community-Detection.git
   ```
2. Install PyTorch
   ```sh
   pip install torch
   ```
3. Install Pytorch Geometric (PyG)
   ```sh
   pip install torch-geometric
   ```
4. Install OGB
   ```sh
   pip install ogb
   ```
5. Install NetworkX
   ```sh
   pip install networkx
   ```
6. Install CDLib
   ```sh
   pip install cdlib
   ```

<!-- USAGE EXAMPLES -->
## Usage

Follow these steps.
* Run the `dataloader.py` to download the dataset in your project folder.
* Run `cdlib_algo_analysis.py` to run different algorithms of cdlib.

<!-- ROADMAP -->
## Roadmap

- [x] Analyze the dataset
- [x] Run different available algorithms and observe performance on our dataset
- [ ] Find Ground Truth communities for our dataset
      
