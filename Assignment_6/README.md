# Assignment 6: Medians, Order Statistics, and Elementary Data Structures

## Overview
This repository contains the full implementation for **Assignment 6**, which covers:

1. **Selection Algorithms**
   - Deterministic Selection (Median of Medians) – Worst-case O(n)
   - Randomized Quickselect – Expected O(n)
   - Full performance analysis + empirical benchmarking

2. **Elementary Data Structures**
   - Arrays
   - Stacks (array-based)
   - Queues (array-based)
   - Singly Linked Lists
   - Optional Tree implementation
   - Complexity analysis + real-world applications

The project includes:
- Source code (`/src`)
- Unit tests (`/tests`)
- APA-formatted report (`Assignment6_Report.pdf`)
- Benchmark results and graphs
- This README with setup instructions and summary

---

##  How to Run the Code

### **1. Clone the Repository**
```bash
git clone https://github.com/agadde37312/MSCS532.git
cd Assignment6

### **2. Create a Virtual Environment**

python3 -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows


### **3. Install Dependencies**

pip install -r requirements.txt


### **4. Run the Algorithms**

python src/deterministic_selection.py
python src/randomized_selection.py


### **5. Run Benchmarks**

python benchmarks/selection_benchmarks.py


### **6. Run Test Cases**

pytest tests -v

---------------------------------

## Summary of Findings (From APA Report)

# Selection Algorithms

Deterministic Median-of-Medians consistently performed in linear worst-case time, especially reliable for adversarial input.

Randomized Quickselect was significantly faster on average and preferred in real-world workloads.

Sorted and reverse-sorted arrays increased Quickselect variability, but deterministic performance remained steady.


## Elementary Data Structures

Array operations were extremely fast for indexed access but expensive for insert/delete in the middle.

Stacks and queues implemented using arrays achieved O(1) push/pop and enqueue/dequeue.

Linked lists performed well for insertion and deletion but poorly for random access.

Each structure demonstrates clear trade-offs appropriate for different real-world scenarios.