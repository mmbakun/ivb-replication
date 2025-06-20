# IVB: Multimodal Adaptive Model with Hierarchical Perceptive Memory and Adaptive Conditional Path

This repository contains replication code for the IVB model, including simplified implementations of the **Hierarchical Perceptive Memory (HPA)** and **Adaptive Conditional Path (ACP)** mechanisms.

## 🧠 Overview

IVB is an adaptive, multimodal AI architecture designed for efficient inference and energy optimization. The system features:
- **HPA** – Context-aware hierarchical memory with short-, mid-, and long-term layers.
- **ACP** – An adaptive computation strategy that selects execution pathways based on task complexity.
- **Multimodal Processing** – Handles text, image, and audio inputs.

## 📁 Repository Contents

- `hpa_module.py` — Minimal implementation of the HPA memory structure.
- `acp_module.py` — Implementation of the Adaptive Conditional Path algorithm.
- `benchmark.py` — Scripts to test inference time and energy-related behavior.
- `README.md` — This file.
- `CITATION.cff` — Citation metadata file.

## 🚀 Quick Start

```bash
git clone https://github.com/your-org/ivb-replication.git
cd ivb-replication
python benchmark.py
```

The scripts simulate task inference and demonstrate conditional activation of memory/computation layers.

## 📚 Citation

If you use this code in your research, please cite:

```
Mieczysław Bakun (2025). IVB: Multimodal Adaptive Model with Hierarchical Perceptive Memory and Adaptive Conditional Path. Zenodo. https://doi.org/10.5281/zenodo.15707361
```

The `CITATION.cff` file is included for citation managers and GitHub integration.

## 🔒 License

This replication code is shared under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

## ✉ Contact

If you are interested in commercial licensing or further collaboration, please contact:

**📧** bakun@ivb-research.edu.pl  
**🌐** https://ivb-research.edu.pl
