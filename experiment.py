from acp.acp_predictor import predict_complexity
from hpa.hpa_core import HPAMemory

# Example prompt
prompt = "What is the capital of France?"

# Feature extraction (very simple example)
features = {
    "length": len(prompt.split()),
    "entropy": 0.3  # placeholder value
}

# Predict complexity class
complexity_class = predict_complexity(features)
print(f"Predicted complexity class: {complexity_class}")

# Get resource activation config
from acp.acp_predictor import get_active_config
config = get_active_config(complexity_class)
print(f"Activated Configuration: {config}")

# Test HPA memory
memory = HPAMemory()
memory.store(prompt)
print("Current memory contents:", memory.retrieve())
