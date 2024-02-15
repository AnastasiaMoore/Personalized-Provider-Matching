import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

# Now you can import from src
from cleaning import clean_dataset
from analysis import perform_analysis
from modeling import build_model
import os

import streamlit as st
import pandas as pd
import numpy as np
# Import other necessary modules

# Load the dataset
#@st.cache
def load_data():
    # Use an absolute path to locate the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, '..', 'data', 'raw', 'providers_data_messy.csv')

    data = pd.read_csv(csv_file_path)
    return data

data = load_data()

# Clean the dataset
#@st.cache

cleaned_data = clean_dataset(data)

# Display the data cleaning results
st.write("Data Cleaning Results", cleaned_data.head())

# Build or load the machine learning model
#@st.cache(allow_output_mutation=True)

model = build_model(cleaned_data)

# Feature engineering and predictions
# Perform any feature engineering required before making predictions
# This might involve calling functions from analysis.py or utils.py

# User input for provider matching
st.header('Find Your Best Healthcare Provider')
# Add Streamlit widgets to let the user input their preferences and health profile

# Perform matching and display results
if st.button('Find Providers'):
    # Use the model to predict the best provider match based on the user's input
    predictions = model.predict(user_input_features)
    # Display the matching providers and any additional information
    st.write("Matching Providers", predictions)

# About section
st.header("About This App")
st.write("""
This app uses machine learning to provide personalized healthcare provider recommendations.
It is designed to demonstrate how data science can be applied to improve healthcare outcomes.
""")

