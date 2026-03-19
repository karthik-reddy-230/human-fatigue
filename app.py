import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier

# ================================
# MOCK MODEL (replace with your trained model)
# ================================
model = RandomForestClassifier()

# ================================
# FEATURE EXTRACTION FUNCTION
# ================================
def extract_features(df):
    delta = df.iloc[:,1].mean()
    theta = df.iloc[:,2].mean()
    alpha = df.iloc[:,3].mean()
    beta  = df.iloc[:,4].mean()

    ratio = (theta + alpha) / (beta + 1e-6)

    return ratio, delta, theta, alpha, beta

# ================================
# UI TITLE
# ================================
st.title("🧠 EEG Fatigue Detection System")

# ================================
# FILE UPLOAD
# ================================
uploaded_file = st.file_uploader("Upload EEG CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("### 📊 Raw Data")
    st.dataframe(df.head())

    # ================================
    # FEATURE EXTRACTION
    # ================================
    ratio, delta, theta, alpha, beta = extract_features(df)

    # ⚠ Dummy prediction (replace with your trained model)
    prob = np.random.randint(0, 100)
    pred = [1 if prob > 60 else 0]

    # ================================
    # FATIGUE GAUGE
    # ================================
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob,
        title={'text': "Fatigue Level (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 40], 'color': 'green'},
                {'range': [40, 70], 'color': 'yellow'},
                {'range': [70, 100], 'color': 'red'}
            ],
            'bar': {'color': 'red'}
        }
    ))

    st.plotly_chart(gauge)

    # ================================
    # FATIGUE ALERT
    # ================================
    if pred[0] == 1:
        st.error("⚠ FATIGUE DETECTED")
    else:
        st.success("✅ NORMAL STATE")

    # ================================
    # EEG MULTI CHANNEL LINE CHART
    # ================================
    fig = go.Figure()

    for col in df.columns[1:6]:
        fig.add_trace(go.Scatter(
            x=df["time"],
            y=df[col],
            mode='lines',
            name=col
        ))

    fig.update_layout(
        title="EEG Time Series (Multiple Channels)",
        xaxis_title="Time",
        yaxis_title="Frequency",
        height=400,
        template="plotly_dark"
    )

    st.plotly_chart(fig)

    # ================================
    # BRAINWAVE POWER CHART
    # ================================
    bands = ['Delta', 'Theta', 'Alpha', 'Beta']
    values = [delta, theta, alpha, beta]

    band_chart = go.Figure()

    band_chart.add_trace(go.Bar(
        x=bands,
        y=values
    ))

    band_chart.update_layout(
        title="Brainwave Band Power",
        template="plotly_dark",
        height=350
    )

    st.plotly_chart(band_chart)