import streamlit as st
import pickle
import numpy as np
import os
from groq import Groq

# Use environment variable for API key for security
api_key = os.environ.get("GROQ_API_KEY", "your_api_key_here")
client = Groq(api_key=api_key)

# Load trained model
model = pickle.load(open("carbon_model.pkl", "rb"))

st.title("🌍 Carbon Footprint Estimator")
st.write("Enter emission factors to predict total emission index")

# User Inputs
transport = st.number_input("Transportation (kgCO2 per km)", 0.0, 1.0, 0.20)
electricity = st.number_input("Electricity (kgCO2 per kWh)", 0.0, 2.0, 0.80)
diet = st.number_input("Diet (kgCO2 per meal)", 0.0, 10.0, 3.0)
waste = st.number_input("Waste (kgCO2 per kg)", 0.0, 2.0, 0.50)
region = st.number_input("Region Factor", 0.5, 2.0, 1.0)

prediction = None

# Predict Button
if st.button("Predict Emission Index"):

    input_data = np.array([[transport, electricity, diet, waste, region]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Total Emission Index: {round(prediction[0],2)}")


def build_prompt(transport, electricity, diet, waste, prediction):

    prompt = f"""
A user has the following carbon emission factors:

Transportation: {transport} kgCO2/km
Electricity: {electricity} kgCO2/kWh
Diet: {diet} kgCO2/meal
Waste: {waste} kgCO2/kg

Total predicted emission index: {prediction:.2f}

Provide:
1. 5 personalized reduction strategies
2. Estimated practical actions
3. Short explanation of environmental impact
4. A sustainability score out of 100
5. Professional but simple language

Keep response structured and clear.
"""

    return prompt


# AI Button
if st.button("Generate AI Reduction Plan"):

    input_data = np.array([[transport, electricity, diet, waste, region]])
    prediction = model.predict(input_data)

    prompt = build_prompt(
        transport,
        electricity,
        diet,
        waste,
        prediction[0]
    )

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

st.subheader("🌱 AI-Generated Sustainability Roadmap")
st.write(response.choices[0].message.content)

messages=[
    {"role": "system", "content": "You are an environmental sustainability expert helping users reduce carbon footprint."},
    {"role": "user", "content": prompt}
]