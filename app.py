import streamlit as st
import joblib
import pandas as pd

model = joblib.load("Electric_Bill_AC_model.pkl")

st.title("Electric Bill Prediction based on AC Units")

ac = st.number_input(
    "Enter the AC Units",
    min_value=1.0,
    max_value=100.0,
    value=1.0
)

if st.button("Predict"):

    if ac < 1 or area > 100:
        st.error("Cannot predict: AC units must be between 1 and 100.")

    else:
        input_data = pd.DataFrame({
            "AC_Units": [ac]
        })
      
        new_data_poly = poly.transform(input_data)
      
        new_pred = model.predict(new_data_poly)
      
        predicted_price = new_pred[0]

        st.success(f"Predicted Electric Bill: ₹{predicted_price:,.2f}")
