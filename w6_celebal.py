# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Set Streamlit page config
st.set_page_config(page_title="ML Model Deployment", layout="centered")

# Load data and model
@st.cache_data
def load_data():
    data = load_iris(as_frame=True)
    df = data.frame
    df['target'] = data.target
    return df, data.feature_names, data.target_names

@st.cache_resource
def train_model(df):
    X = df.iloc[:, :-1]
    y = df['target']
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model

# Load and train model
df, feature_names, target_names = load_data()
model = train_model(df)

# Sidebar inputs
st.sidebar.header("Input Features")
input_data = []
for feature in feature_names:
    val = st.sidebar.slider(
        label=feature,
        min_value=float(df[feature].min()),
        max_value=float(df[feature].max()),
        value=float(df[feature].mean())
    )
    input_data.append(val)

# Convert input to DataFrame
input_df = pd.DataFrame([input_data], columns=feature_names)

# Prediction
prediction = model.predict(input_df)[0]
proba = model.predict_proba(input_df)[0]

# Display results
st.title("🌼 Iris Species Classifier")
st.write("Input Features:")
st.dataframe(input_df)

st.subheader("Prediction:")
st.success(f"Predicted Class: **{target_names[prediction]}**")

st.subheader("Prediction Probability:")
prob_df = pd.DataFrame(proba.reshape(1, -1), columns=target_names)
st.dataframe(prob_df)

# Plot probability
fig, ax = plt.subplots()
sns.barplot(x=target_names, y=proba, palette="viridis", ax=ax)
plt.title("Prediction Probabilities")
plt.ylabel("Probability")
st.pyplot(fig)

# Bonus: Show raw dataset
with st.expander("Show Full Dataset"):
    st.dataframe(df)
