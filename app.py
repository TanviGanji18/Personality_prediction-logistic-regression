import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# -----------------------------
# UI
# -----------------------------
st.title("🧠 Personality Predictor")
st.write("Predict Introvert or Extrovert")

# Inputs
time_alone = st.slider("Time spent alone", 0, 12, 4)
stage_fear = st.selectbox("Stage fear?", ["Yes", "No"])
social_events = st.slider("Social event attendance", 0, 10, 5)
going_outside = st.slider("Going outside frequency", 0, 10, 5)
drained = st.selectbox("Drained after socializing?", ["Yes", "No"])
friends = st.slider("Friends circle size", 0, 15, 5)
posts = st.slider("Post frequency", 0, 10, 3)

# Convert categorical → numeric
stage_fear = 1 if stage_fear == "Yes" else 0
drained = 1 if drained == "Yes" else 0

# Prediction
if st.button("Predict"):
    input_data = np.array([[time_alone, stage_fear, social_events,
                            going_outside, drained, friends, posts]])

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("🎉 Extrovert")
    else:
        st.success("🧘 Introvert")