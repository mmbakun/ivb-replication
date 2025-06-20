# IVB: Multimodal Adaptive Model with Hierarchical Aperceptive Memory (HPA)

This repository provides a simplified, research-oriented implementation of the key components described in the IVB paper.
The purpose of this code is to **replicate** the core experimental results while protecting proprietary production-level optimizations.

## 📦 Contents

- `hpa/`: Core logic for Hierarchical Aperceptive Memory
- `acp/`: Implementation of the Adaptive Conditional Path (ACP) mechanism
- `benchmarks/`: Scripts for the MM-QA40 and Energy-Edge benchmarks
- `models/`: Pretrained weights (e.g., IVB_3PLEX_TRUE_L_2)

## 🚀 Running Experiments

```bash
bash run_experiments.sh
```

This will execute the core benchmarks and reproduce the results shown in Table 4.1 of the paper.

## 🔒 Disclaimer

This code is **not production code**. It is provided solely for academic and research purposes to support the reproducibility of results.
Optimized, full-scale implementations remain proprietary and protected as trade secrets.

For licensing or collaboration inquiries, contact: license@ivbeing.com
