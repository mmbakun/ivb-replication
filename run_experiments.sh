#!/bin/bash
echo "Running MM-QA40 benchmark..."
python3 benchmarks/mm_qa40.py

echo "Running Energy-Edge benchmark..."
python3 benchmarks/energy_edge.py
