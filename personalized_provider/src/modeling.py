# modeling.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def build_model(cleaned_data):
    # Assuming 'cleaned_data' is a pandas DataFrame with appropriate preprocessing done.

    # Split your data into features and target
    X = cleaned_data.drop(columns=['Target'])  # Replace 'Target' with the name of your target column
    y = cleaned_data['Target']

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a machine learning pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Evaluate the model
    y_pred = pipeline.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

    # Return the trained pipeline
    return pipeline

