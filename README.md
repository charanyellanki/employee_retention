# Employee Retention Predictor

This project consists of a Streamlit application for predicting employee retention based on various factors, and a logistic regression model trained on an employee dataset. The dataset contains information about employees in a company, including their educational backgrounds, work history, demographics, and employment-related factors. It has been anonymized to protect privacy while still providing valuable insights into the workforce.

## Dataset Description

This is a Kaggle dataset: https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset

This dataset contains the following columns:

- **Education:** The educational qualifications of employees, including degree, institution, and field of study.
- **Joining Year:** The year each employee joined the company, indicating their length of service.
- **City:** The location or city where each employee is based or works.
- **Payment Tier:** Categorization of employees into different salary tiers.
- **Age:** The age of each employee, providing demographic insights.
- **Gender:** Gender identity of employees, promoting diversity analysis.
- **Ever Benched:** Indicates if an employee has ever been temporarily without assigned work.
- **Experience in Current Domain:** The number of years of experience employees have in their current field.
- **Leave or Not:** A binary target column indicating whether an employee leaves the company or not.


## Application Description

The Streamlit application allows users to input various employee attributes such as gender, city, age, education level, joining year, experience in the current domain, payment tier, and whether the employee has ever been benched. Based on these inputs, the application predicts whether the employee will potentially leave the company or is willing to work in the company.

## Tools Used

- **Streamlit:** Used for creating the user interface to input data for model predictions.
- **MLflow:** Used for experiment tracking and model registry.
- **Azure Cloud:** Used for application and model deployment.

## Requirements

You can install these dependencies using `pip install -r requirements.txt`.
