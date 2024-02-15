import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def clean_dataset(data):
    # Convert provider names to title case and strip any leading/trailing whitespace
    data['ProviderName'] = data['ProviderName'].str.title().str.strip()

    # Replace negative years of experience with their absolute values
    data['YearsOfExperience'] = data['YearsOfExperience'].abs()

    # Fill in missing values for years of experience with the column's average
    # Make sure to skip NaN values in the average calculation
    avg_years = data['YearsOfExperience'].mean(skipna=True)
    data['YearsOfExperience'].fillna(avg_years, inplace=True)

    # Standardize location to title case
    data['Location'] = data['Location'].str.title()

    # Correct out-of-range patient satisfaction scores
    data['PatientSatisfactionScore'] = data['PatientSatisfactionScore'].apply(
        lambda x: min(max(x, 1), 10) if pd.notnull(x) else x
    )

    # Remove duplicates based on certain criteria
    data.drop_duplicates(subset=['ProviderName', 'Specialization', 'Location'], keep='first', inplace=True)

    # Normalize specialization entries (example provided, expand as needed)
    specializations_to_replace = {'GP': 'General Practice', 'gen practice': 'General Practice'}
    data['Specialization'].replace(specializations_to_replace, inplace=True)

    # Handle treatment cost outliers
    # Example: Cap treatment cost at a maximum value
    data['TreatmentCost'] = data['TreatmentCost'].apply(lambda x: x if x <= 10000 else 10000)

    # Additional code to calculate the composite score
    weight_satisfaction = 0.4
    weight_cost = -0.2  # Negative because higher cost is typically less desirable
    weight_success = 0.4

    # Calculate composite score
    data['CompositeScore'] = (
        data['PatientSatisfactionScore'] * weight_satisfaction
        - data['TreatmentCost'] * weight_cost
        + data['SuccessfulTreatments'] * weight_success
    )

    # Normalize or scale CompositeScore if necessary
    # For example, using MinMaxScaler
    scaler = MinMaxScaler()
    data['NormalizedCompositeScore'] = scaler.fit_transform(data[['CompositeScore']])

    # Return the cleaned and transformed dataset
    return data
