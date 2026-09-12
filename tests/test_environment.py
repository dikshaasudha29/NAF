import pandas
import numpy
import sklearn
import scapy
import shap
import streamlit
import yaml
import torch

print("Pandas:", pandas.__version__)
print("NumPy:", numpy.__version__)
print("Scikit-learn:", sklearn.__version__)
print("Scapy:", scapy.__version__)
print("SHAP:", shap.__version__)
print("Streamlit:", streamlit.__version__)
print("PyYAML:", yaml.__version__)
print("PyTorch:", torch.__version__)

print("\nPyTorch CPU available:", torch.cuda.is_available() is False)
print("Environment setup successful.")