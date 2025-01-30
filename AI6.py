# =============================================================================
# NASA AERODYNAMIC ANALYSIS - MULTIPLE LINEAR REGRESSION
# =============================================================================
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# =============================================================================
# 1. VERIFY FILE PATH AND LOAD DATA
# =============================================================================
# Define file paths
input_path = r"C:\Users\jonat\Downloads\visual\A1.3 NASA.csv"
output_dir = r"C:\Users\jonat\Downloads\visual"
output_path = os.path.join(output_dir, "NASA_Results.csv")

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Verify input file exists
if not os.path.exists(input_path):
    print(f"ERROR: Input file '{input_path}' not found")
    exit()

# Load dataset
df = pd.read_csv(input_path)
print("1. DATA FRAME DIMENSIONS:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

# =============================================================================
# 2. DATA PREPARATION AND SAVING
# =============================================================================
try:
    # Clean data
    df['espesor'] = df['espesor'].replace(0, 1e-6)
    
    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"2. CLEANED DATA SAVED TO:\n{output_path}")
    print(f"File verification: {'Exists' if os.path.exists(output_path) else 'FAILED'}")

except Exception as e:
    print(f"ERROR SAVING FILE: {str(e)}")
    exit()

# Rest of your existing code remains the same...
# [Keep all the existing code for model training, evaluation, and visualization]