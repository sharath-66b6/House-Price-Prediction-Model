import streamlit as st
import joblib
import numpy as np
model = joblib.load('house_price_model.pkl')
st.title('House Price Prediction')
type = st.number_input('Type (MSSubClass)', min_value=1, max_value=190)
area = st.number_input('Area (LotArea)', min_value=500, max_value=50000)
rating = st.number_input('Overall Condition (1-10)', min_value=1, max_value=10)
year_built = st.number_input('Year Built', min_value=1800, max_value=2024)
bathrooms = st.number_input('Total Bathrooms', min_value=0, max_value=10)
bedrooms = st.number_input('Total Bedrooms', min_value=0, max_value=10)
kitchens = st.number_input('Total Kitchens ', min_value=0, max_value=5)
if st.button('Predict'):
    features = np.array([[type, area, rating, year_built, bathrooms, bedrooms, kitchens]])
    predicted_price = model.predict(features) 
    st.write(f'The predicted house price is: ${predicted_price[0]:,.2f}')
