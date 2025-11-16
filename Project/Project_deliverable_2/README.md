# Recommendation System PoC - Phase 2

## Overview
This repository contains a partial implementation (proof of concept) of a hybrid recommendation system combining collaborative filtering and content-based approaches. The system is designed to demonstrate core data structures such as:

- Sparse user–item interaction matrix
- Latent factor embeddings
- Approximate Nearest Neighbor (ANN) index using LSH
- Item–item similarity index

The implementation is in Python and supports basic insertion, retrieval, and top-k recommendation queries.

---

## Folder Structure

project/
└── project_deliverable_2/
    ├── README.md
    ├── requirements.txt
    ├── recommender/
    │   ├── __init__.py
    │   └── recommender.py
    └── benchmarks/
        └── benchmark_recommender.py
