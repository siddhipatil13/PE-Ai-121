import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(page_title="House Price Predictor", page_icon="🏡", layout="centered")

st.title(" Linear Regression – House Price Prediction")
st.write("Enter the house details below to predict its price using a Linear Regression model.")

# ---------------------------------
# Sample Training Data (fake dataset)
# ---------------------------------
data = {
    'area': [1000, 1500, 1800, 2400, 3000],
    'bedrooms': [2, 3, 3, 4, 5],
    'age': [10, 5, 8, 3, 1],
    'price': [200000, 300000, 350000, 450000, 600000]
}
df = pd.DataFrame(data)

# Features and target
X = df[['area', 'bedrooms', 'age']]
y = df['price']

# Train Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# ---------------------------------
# User Inputs
# ---------------------------------
st.subheader(" Enter House Details")

area = st.number_input("Enter area (in sq ft):", min_value=500, max_value=5000, value=1500)
bedrooms = st.slider("Number of bedrooms:", 1, 6, 3)
age = st.number_input("House age (in years):", min_value=0, max_value=50, value=5)

# ---------------------------------
# Prediction
# ---------------------------------
if st.button(" Predict Price"):
    input_data = np.array([[area, bedrooms, age]])
    predicted_price = model.predict(input_data)[0]
    st.success(f" Estimated House Price: **${predicted_price:,.2f}**")

# ---------------------------------
# Info Section
# ---------------------------------
st.markdown("""
###  About Linear Regression
Linear Regression is a **supervised machine learning algorithm** used to predict **continuous values**.
It finds the best-fit line that relates input variables (like area, bedrooms, age) to the output variable (price).

**Equation:**
> Price = m₁(Area) + m₂(Bedrooms) + m₃(Age) + b
""")
