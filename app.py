import streamlit as st
import joblib
import numpy as np

# 1. Load the trained Deep Learning model and vectorizer
model = joblib.load('fake_job_model_dnn.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# 2. Configure the page
st.set_page_config(page_title="Fake Job Detector", page_icon="🛡️")

st.title("🛡️ Fake Job Posting Detection System (DL Edition)")
st.write("Enter a job description below to verify its authenticity using our Multi-Layer Perceptron Deep Neural Network.")

# 3. User Input Area
job_text = st.text_area("Paste Job Description Here:", height=250)

# 4. Prediction Logic
if st.button("Analyze Job Posting"):
    if job_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Preprocess input
        transformed_text = vectorizer.transform([job_text.lower()])
        
        # Get the strict prediction from the Neural Network
        prediction = model.predict(transformed_text)
        
        st.divider()
        
        # Display Results
        if prediction == 1:
            st.error("🚨 FAKE JOB ALERT: This posting has been flagged as fraudulent.")
            st.info("⚠️ **Why?** Our Deep Neural Network detected complex semantic patterns and hidden correlations commonly found in scam postings.")
        else:
            st.success("✅ REAL JOB: This posting appears to be safe.")
            st.info("🛡️ The Deep Neural Network verified this text against standard, legitimate job requirements.")