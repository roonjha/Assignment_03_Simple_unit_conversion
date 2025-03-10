import streamlit as st
import time

conversion_factors = {
    'Length': {
        'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000,
        'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701,
        'nautical miles': 0.000539957
    },
    'Weight': {
        'grams': 1, 'kilograms': 0.001, 'milligrams': 1000, 'pounds': 0.00220462,
        'ounces': 0.035274, 'tons': 0.00000110231, 'carats': 5, 'stones': 0.000157473
    },
    'Volume': {
        'liters': 1, 'milliliters': 1000, 'cubic meters': 0.001, 'cubic centimeters': 1000,
        'gallons': 0.264172, 'quarts': 1.05669, 'pints': 2.11338, 'cups': 4.22675,
        'fluid ounces': 33.814, 'barrels': 0.00628981
    },

}

# unit conversion ka function perform kerney k liye...example temperature to Celsius

def convert_units(value, from_unit, to_unit, category):
    if category == 'Temperature':
        return conversion_factors[category][to_unit](value) if from_unit == 'Celsius' else None
    return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# yeh page setting configuration k liye he.
st.set_page_config(page_title="Growth Mind Challenge - Assignment No. 02", layout="centered")

#col1 and col2 user se unit ki selection k variables he  or converter ki selection kerna or phir usey value ko ko print kerwana

st.title("Unit Converter")
category = st.selectbox("Select Category", list(conversion_factors.keys()), index=0)
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", list(conversion_factors[category].keys()))
with col2:
    to_unit = st.selectbox("To Unit", list(conversion_factors[category].keys()))
value = st.number_input("Enter Value to Convert", value=0.0, step=0.1)   

# Convert and Reset buttons (Yeh col1 and col2 unit ko convert kerna button phir inhi unit ko reset kerne k liye)
col1, col2 = st.columns(2)
with col1:
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"Converted Value: {result} {to_unit}")
        st.session_state.result = result 
with col2:
    if st.button("Reset", key="reset", help="Click to reset inputs", use_container_width=True):
        st.session_state.result = None  #  result ko clear kerney k liye
        st.rerun()

