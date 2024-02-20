import streamlit as st
import requests

def get_prediction(input_data):
    # Local MLflow model serving endpoint
    API_URL = "http://127.0.0.1:5000/invocations"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(API_URL, json=input_data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        prediction = response.json()
        print("Prediction response:", prediction)  # Print the prediction response
        return prediction['predictions'][0]
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None
    except (KeyError, ValueError) as e:
        st.error(f"Error processing prediction response: {e}")
        return None

def main():
    st.title('Employee Retention Predictor')
    st.caption('This app helps you provide inputs to get output weather a employee stays in the company or not')

    # Define input fields
    gender = st.radio('Gender', ['Male', 'Female'])
    city = st.selectbox('Select the city', ['Bangalore', 'Pune', 'New Delhi'])
    age = st.slider('Age', 0, 70)
    payment = st.select_slider('Payment Tier', [1, 2, 3])
    education = st.selectbox('Education level', ['Bachelors', 'Masters', 'PHD'])
    year = st.number_input('Enter Joining Year', step=1, value=None, format="%d")
    experience = st.number_input('Experience In Current Domain', step=1, value=None, format="%d")
    benched = st.radio('Ever Benched', ['Yes', 'No'])

    # When user clicks the 'Predict' button
    if st.button("Predict"):
        # Prepare input data
        input_data = {
            "dataframe_split": {
                "columns": ['Education', 'JoiningYear', 'City', 'PaymentTier', 'Age', 'Gender', 'EverBenched', 'ExperienceInCurrentDomain'],
                "data": [[education, year, city, payment, age, gender, benched, experience]]
            }
        }
        # Get prediction
        prediction = get_prediction(input_data)
        # Display prediction
        if prediction is not None:
            if prediction == 0:
                st.write("Employee will potentially leave the company 😞")
            elif prediction == 1:
                st.write("Employee is willing to work in the company 😊")
        else:
            st.error("Failed to get prediction. Please check your input data and try again.")

if __name__ == "__main__":
    main()
