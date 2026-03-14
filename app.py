import streamlit as st
import joblib
import numpy as np

# 1. Load the trained model and vectorizer
model = joblib.load('fake_job_model_svm.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# 2. Configure the page
st.set_page_config(page_title="Fake Job Detector", page_icon="🛡️")

st.title("🛡️ Fake Job Posting Detection System (V2.0)")
st.write("Enter a job description below to verify its authenticity using our Support Vector Machine.")

# 3. User Input Area
job_text = st.text_area("Paste Job Description Here:", height=250)

# 4. Prediction Logic
if st.button("Analyze Job Posting"):
    if job_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Preprocess input
        transformed_text = vectorizer.transform([job_text.lower()])
        
        # Get the strict mathematical prediction from the SVM
        prediction = model.predict(transformed_text)[0]
        
        st.divider()
        
        # Display Results based on the SVM margin boundary
        if prediction == 1:
            st.error("🚨 FAKE JOB ALERT: This posting has been flagged as fraudulent.")
            st.info("⚠️ **Why?** The SVM model mapped this text to the positive side of our decision boundary, detecting semantic patterns commonly found in scam postings.")
        else:
            st.success("✅ REAL JOB: This posting appears to be safe.")
            st.info("🛡️ The SVM model mapped this text to the negative side of our decision boundary, indicating standard, legitimate job requirements.")

# To run the site type into terminal: streamlit run app.py