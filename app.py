```python
import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Load model
model = joblib.load("Electric_Bill_AC_model.pkl")

# Polynomial transformation
poly = PolynomialFeatures(degree=2)
poly.fit([[1]])

st.title("Electric Bill Prediction based on AC Units")

# Allow values below 1 so we can show our own error message
ac = st.number_input(
    "Enter the AC Units",
    min_value=0.0,
    value=1.0,
    step=1.0
)

if st.button("Predict"):

    # Validate input FIRST
    if ac < 1 or ac > 150:
        st.error("Cannot predict: AC units must be between 1 and 150.")

    else:
        # Only valid values reach this section
        input_data = pd.DataFrame({
            "AC_Units": [ac]
        })

        new_data_poly = poly.transform(input_data)

        new_pred = model.predict(new_data_poly)

        predicted_price = new_pred[0]

        st.success(
            f"Predicted Electric Bill: ₹{predicted_price:,.2f}"
        )
```
