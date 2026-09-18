import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

model = joblib.load("Electric_Bill_AC_Fan_model.pkl")

poly = PolynomialFeatures(degree=2)
poly.fit([[1, 1]])

st.title("Electric Bill Prediction based on AC and Fan Units")

ac = st.number_input(
    "Enter the AC Units",
    min_value=0.0,
    value=1.0,
    step=1.0
)

fan = st.number_input(
    "Enter the Fan Units",
    min_value=0.0,
    value=1.0,
    step=1.0
)

# other = st.number_input(
#     "Enter the Other Units",
#     min_value=0.0,
#     value=1.0,
#     step=1.0
# )

if st.button("Predict"):

    if ac < 1 or ac > 150:
        st.error("Cannot predict: AC units must be between 1 and 150.")
        
    elif fan < 1 or fan > 150:
        st.error("Cannot predict: Fan units must be between 1 and 150.")

    # elif other < 1 or other > 150:
    #     st.error("Cannot predict: Fan units must be between 1 and 150.")
        
    else:
        input_data = pd.DataFrame({
            "AC_Units": [ac],
            "Fan_Units": [fan],
            # "Other_Units": [other]
        })

        new_data_poly = poly.transform(input_data)

        new_pred = model.predict(new_data_poly)

        predicted_price = new_pred[0]

        st.success(
            f"Predicted Electric Bill: ₹{predicted_price:,.2f}"
        )
