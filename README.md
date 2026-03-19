# Quantum ML Classifier — Project 1

<div align="center">

![IBM Quantum](https://img.shields.io/badge/IBM%20Quantum-052FAD?style=flat-square&logo=ibm&logoColor=white)
![Qiskit ML](https://img.shields.io/badge/Qiskit%20ML-0.7.2-6929C4?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-4fc3f7?style=flat-square)
![Python 3.9](https://img.shields.io/badge/Python%203.9-1a1a2e?style=flat-square&logo=python&logoColor=4fc3f7)
![License](https://img.shields.io/badge/License-MIT-00ff88?style=flat-square)
![Release](https://img.shields.io/badge/Release-v1.0-4fc3f7?style=flat-square)

</div>

<br/>

<div align="center">
<i>Project 1 of 3 · IBM Quantum 20-Day Learning Sprint · VIT Chennai</i>
</div>

---

## Overview

This project compares three classifiers on the MNIST binary digit recognition task — classical SVM, quantum SVM, and a fully variational quantum classifier. The goal is to establish where quantum methods match, fall short of, or exceed classical baselines on a real dataset.

| Method | Kernel / Model | Accuracy | Training Time |
|--------|---------------|----------|---------------|
| Classical SVM | RBF | 100.00% | 0.013s |
| QSVM | ZZFeatureMap | 100.00% | 2.585s |
| VQC | RealAmplitudes | 93.33% | 467.96s |

---

## The Problem

MNIST contains 70,000 handwritten digit images. This project uses a binary subset — digit 0 vs digit 1 — processed into a manageable format for quantum classification.

```
Full MNIST    →  70,000 samples · 784 features · 10 classes
This project  →  200 samples · 2 features (PCA) · 2 classes
```

PCA reduces the 64-dimensional digit features to 2 principal components. MinMaxScaler normalizes them to [0, 1] for quantum circuit compatibility.

---

## Methods

### Classical SVM

Support Vector Machine with RBF kernel. Standard scikit-learn implementation. Used as the performance and speed baseline.

```
Train time : 0.013s
Accuracy   : 100.00%  (60/60 test samples)
```

---

### QSVM — Quantum Support Vector Machine

The RBF kernel is replaced with a quantum kernel computed using ZZFeatureMap. The SVM framework remains classical — only the kernel computation moves to the quantum circuit.

```
Feature map : ZZFeatureMap (2 qubits, reps=2)
Kernel      : FidelityStatevectorKernel
Train time  : 2.585s
Accuracy    : 100.00%  (60/60 test samples)
```

The ZZFeatureMap encodes each data point as:

```
Step 1: H gates → equal superposition
Step 2: P(2x₀), P(2x₁) → encode features
Step 3: CX → P(2(π-x₀)(π-x₁)) → CX → encode interactions
Applied twice (reps=2)
```

The quantum kernel is then:
```
K(x, y) = |⟨ψ(x)|ψ(y)⟩|²
```

---

### VQC — Variational Quantum Classifier

The entire model is a parameterized quantum circuit. No SVM involved. ZZFeatureMap encodes the data; RealAmplitudes provides 8 trainable parameters optimized by COBYLA.

```
Feature map : ZZFeatureMap (2 qubits, reps=2)
Ansatz      : RealAmplitudes (2 qubits, reps=3)
Parameters  : 8 trainable (θ[0]...θ[7])
Optimizer   : COBYLA (150 iterations)
Train time  : 467.96s
Accuracy    : 93.33%  (56/60 test samples)
Final loss  : 0.4349


Loss steadily decreased across all 150 iterations — convergence not yet complete. Extended training would likely push VQC accuracy above 95%.


## Key Findings

QSVM matched classical SVM exactly on MNIST — both achieved 100% accuracy. This is a stronger result than the Iris experiment (Days 8–9) where QSVM scored 90%. The MNIST digit boundary is more complex, and the quantum feature map captured it as effectively as the RBF kernel.

VQC at 93.33% is significantly better than its 60% result on Iris. A harder dataset with a more complex decision boundary gives the variational approach more room to work. The loss curve had not plateaued at 150 iterations — additional training would improve accuracy further.

Training time scales dramatically:
```
Classical SVM :   0.013s  →  practical for any dataset
QSVM          :   2.585s  →  acceptable for moderate datasets
VQC           : 467.960s  →  requires careful iteration budget
```

---

## Project Structure
'''
```
IBM_QuantumFoundation_Day10/
│
├── notebooks/
│   └── 01_qml_classifier.ipynb    ← main experiment
│
├── src/
│   └── qml_utils.py               ← data loading utilities
│
├── results/
│   └── qml_comparison.png         ← all plots
│
├── data/                          ← gitignored
├── docs/
├── LICENSE                        ← MIT
├── requirements.txt
├── .gitignore
└── README.md
```
'''
---

## Setup

```bash
conda create -n qml_fresh python=3.9 -y
conda activate qml_fresh
pip install qiskit==0.45.3 qiskit-aer==0.13.3 qiskit-machine-learning==0.7.2 qiskit-algorithms==0.3.0 scikit-learn matplotlib numpy scipy jupyter
jupyter notebook
```

Open `notebooks/01_qml_classifier.ipynb` and run all cells.

---

## Tech Stack

```python
qiskit                == 0.45.3
qiskit-aer            == 0.13.3
qiskit-machine-learning == 0.7.2
qiskit-algorithms     == 0.3.0
scikit-learn          >= 1.0.0
matplotlib            >= 3.7.0
numpy                 >= 1.24.0
scipy                 >= 1.10.0
```

---

## Sprint Progress

```
Day 01  ──  ✅  Qiskit setup · Hello Quantum · first IBM cloud circuit
Day 02  ──  ✅  Superposition · Entanglement · Multi-gate circuits
Day 03  ──  ✅  Gates deep-dive · Grover's algorithm
Day 04  ──  ✅  VQE · parametric circuits · COBYLA optimizer
Day 05  ──  ✅  QAOA · MaxCut · optimal partition found
Day 06  ──  ✅  Quantum Error Mitigation · noise models · ZNE
Day 07  ──  ✅  All 5 experiments on real IBM hardware · ibm_torino
Day 08  ──  ✅  QSVM · ZZFeatureMap · Iris dataset
Day 09  ──  ✅  VQC · Variational Quantum Classifier · Iris dataset
Day 10  ──  ✅  Project 1 · QML Classifier · MNIST · v1.0 release
Day 11  ──  ⬡   Quantum Safe Cryptography · post-quantum crypto
·
·
Day 20  ──  ·   Final push 
```

---

## License


---

<div align="center">

[![GitHub](https://img.shields.io/badge/Akhila707-181717?style=flat-square&logo=github)](https://github.com/Akhila707)
&nbsp;·&nbsp;
[![IBM Quantum](https://img.shields.io/badge/IBM%20Quantum-052FAD?style=flat-square&logo=ibm&logoColor=white)](https://quantum.ibm.com)

</div>
