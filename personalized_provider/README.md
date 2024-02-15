# Healthcare Provider Insight
Choosing the right healthcare provider is a decision that affects health outcomes, financial stability, and overall well-being. Yet, navigating through a sea of healthcare options can be overwhelming for patients and employers alike. "Healthcare Provider Insight" is an application designed to simplify this process by providing a comprehensive evaluation of healthcare providers based on data-driven insights.

# App Features
* Provider Evaluation: Using advanced machine learning algorithms, the app assesses healthcare providers across multiple dimensions, including quality of care, patient satisfaction, and cost-efficiency.

* Personalized Matching: By analyzing patient profiles and medical histories, the app matches individuals with providers who are best suited to their specific health needs, ensuring personalized care recommendations.

* Outcome Predictions: The app predicts potential health outcomes and recovery times, allowing patients to make informed decisions based on expected treatment success rates.

* Cost Transparency: Understand potential costs upfront. The app provides estimates of treatment expenses, helping patients manage their healthcare budgets more effectively.

* Quality Rankings: Providers are ranked based on performance metrics derived from patient outcomes, satisfaction surveys, and cost data, fostering a competitive environment that rewards top-performing doctors.


# About the Data

The app utilizes a synthetic dataset reflecting typical healthcare provider metrics. The dataset includes:

* Provider names and specialties
* Years of experience
* Location-based practices
* Average patient recovery times
* Patient satisfaction scores
* Treatment costs and success rates
  
This dataset has been purposefully designed to be 'messy,' mimicking real-world data challenges such as typos, missing values, and outliers. 

## Data Cleaning Process

The data cleaning process is defined in the `sql/data_cleaning.sql` script. It includes the following steps:

- Standardization of provider names to a consistent format.
- Filling in missing values for years of experience with the column average.
- Correction of negative values in the years of experience.
- Standardization of location names.
- Normalization of patient satisfaction scores to the correct range.
- Deduplication of provider records.
- Capping treatment costs to remove outliers.
- Normalization of specialization names.

To run these cleaning steps, you would execute the SQL script against the dataset in an SQL-compatible database environment. The script is designed for a PostgreSQL database but can be adapted for other database systems if necessary.


# The Technology

At the heart of "Healthcare Provider Insight" is a robust machine learning framework capable of processing complex datasets to deliver actionable insights. The technology stack includes:

* Python for backend processing and analytics
* SQL for data querying and cleanup
* Streamlit for an intuitive user interface
* Scikit-learn for predictive modeling

  
