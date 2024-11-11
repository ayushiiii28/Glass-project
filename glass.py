import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Loading the trained model (replace the path with your actual model file)
pickle_in = open('model_pickle.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Function to make predictions
def prediction(RI, Na, Mg, Al, Si, K, Ca, Ba, Fe):
    prediction = classifier.predict([[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]])
    return prediction

# Streamlit app code
def main():
    # Set title for the Streamlit app
    st.title("Glass Type Prediction")

    # Add some description or styling
    st.markdown("""
    <div style="background-color:yellow;padding:13px">
    <h1 style="color:black;text-align:center;">Streamlit Glass Prediction Model</h1>
    </div>
    """, unsafe_allow_html=True)

    # Input fields for features (user input for prediction)
    st.header("Enter the values for Glass Features")

    RI = st.number_input("Refractive Index (RI)", value=1.5, step=0.01)
    Na = st.number_input("Sodium (Na)", value=10, step=1)
    Mg = st.number_input("Magnesium (Mg)", value=2, step=1)
    Al = st.number_input("Aluminum (Al)", value=1, step=1)
    Si = st.number_input("Silicon (Si)", value=70, step=1)
    K = st.number_input("Potassium (K)", value=0, step=1)
    Ca = st.number_input("Calcium (Ca)", value=8, step=1)
    Ba = st.number_input("Barium (Ba)", value=0, step=1)
    Fe = st.number_input("Iron (Fe)", value=0, step=1)

    # When 'Predict' button is pressed
    if st.button("Predict"):
        result = prediction(RI, Na, Mg, Al, Si, K, Ca, Ba, Fe)
        st.success(f'The predicted glass type is: {result[0]}')

if __name__ == '__main__':
    main()
