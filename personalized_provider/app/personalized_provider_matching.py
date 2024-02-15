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
@st.cache
def load_data():
    # Use an absolute path to locate the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, '..', 'data', 'raw', 'providers_data_messy.csv')

    data = pd.read_csv(csv_file_path)
    return data

# Load the dataset
data = load_data()  

@st.cache
def get_cleaned_data():
    """
    Load, clean, and return the dataset ready for analysis and modeling.
    
    The function uses caching to avoid re-loading and re-cleaning the data
    each time the Streamlit app is refreshed.
    
    Returns:
        DataFrame: The cleaned dataset.
    """
    # Load the dataset
    data = load_data()  # load_data() is called here

    # Clean the dataset using the clean_dataset function from the cleaning module
    cleaned_data = clean_dataset(data)  # clean_dataset() is called here with the loaded data

    return cleaned_data

# No need to pass 'data' since 'get_cleaned_data' will call 'load_data()' within it
cleaned_data = get_cleaned_data()

# Build or load the machine learning model
@st.cache(allow_output_mutation=True)
def get_model(cleaned_data):
    return build_model(cleaned_data)

model = get_model(cleaned_data)

# Create tabs
tab1, tab2 = st.tabs(["App", "About"])

# App tab content
with tab1:
    st.header('Find Your Best Healthcare Provider')
    
    # Add Streamlit widgets to let the user input their preferences and health profile
    # User input code goes here
    # For example:
    # age = st.number_input('Age', min_value=0, max_value=120, value=30)
    # ... other inputs ...

    # Perform matching and display results
    if st.button('Find Providers'):
        # Assuming you have a function to transform user inputs into features for the model
        # user_input_features = transform_user_input_to_features(age, ...)
        # predictions = model.predict(user_input_features)
        
        # Placeholder for prediction output
        predictions = ['Provider A', 'Provider B', 'Provider C']
        
        # Display the matching providers and any additional information
        st.write("Matching Providers", predictions)

# About tab content
with tab2:
    st.write("""
    ## About This App
    
    This app uses machine learning to provide personalized healthcare provider recommendations.
    It is designed to demonstrate how data science can be applied to improve healthcare outcomes.
    
    ## How It Works
    
    Users enter their personal health profile and preferences. The app then uses a machine learning model to match them with healthcare providers that best meet their needs, based on historical data on provider performance, patient outcomes, and treatment costs.
    
    ## Data Cleaning
    
    The initial dataset is processed through a series of cleaning steps to ensure the quality and reliability of the data used to train the machine learning model.
    
    ## Predictive Modeling
    
    The app utilizes a predictive model that has been trained on the cleaned dataset. This model takes user inputs as features to predict and recommend the top healthcare providers.
    
    ## Try It Out
    
    Use the 'App' tab to input your information and find out which healthcare providers are best for you!
    """)

# Portfolio tab content
with st.tabs("Methodology"):
    st.write("""
    ## Project Portfolio: Healthcare Provider Insight

    ### Overview
    - **Objective**: Briefly summarize the goal of creating the Healthcare Provider Insight app.
    - **Motivation**: Explain why you chose to work on this project and how it aligns with Garner Health’s mission.

    ### Data Analysis & Cleaning
    - **Data Exploration**: Discuss how you explored the data and any interesting insights you found.
    - **Cleaning Process**: Outline the steps you took to clean the data, challenges faced, and how you overcame them.
    - **Tools & Technologies Used**: List the tools and technologies you used for data cleaning (e.g., SQL, Python libraries).

    ### Predictive Modeling
    - **Model Selection**: Describe the machine learning models you considered and why you chose the final model.
    - **Feature Engineering**: Discuss any features you engineered and why they are important for the model.
    - **Model Performance**: Share how you evaluated the model’s performance (e.g., accuracy, precision, recall).

    ### App Development
    - **Streamlit**: Elaborate on why you chose Streamlit for the app and the benefits it provided.
    - **User Interface**: Discuss the design choices you made for the app’s user interface.
    - **Interactivity**: Highlight the interactive elements of the app (e.g., sliders, buttons, inputs).

    ### Challenges & Learnings
    - **Challenges**: Share significant challenges you encountered while working on the project and how you solved them.
    - **Learnings**: Reflect on what you learned during the project and how it has helped you grow as a data scientist.

    ### Future Improvements
    - **Next Steps**: Outline the potential next steps to improve the app further.
    - **Features Wishlist**: List any additional features you would like to add to the app in the future.

    ### Contact Information
    - Provide your contact details for prospective employers or collaborators to reach out to you.
    """)
