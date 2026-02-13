import streamlit as st
import joblib
import numpy as np

# 1. Load the trained model and vectorizer
# (These files were created by the notebook you just ran)
model = joblib.load('fake_job_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# 2. Configure the page
st.set_page_config(page_title="Fake Job Detector", page_icon="🛡️")

st.title("🛡️ Fake Job Posting Detection System")
st.write("Enter a job description below to verify its authenticity.")

# 3. User Input Area
job_text = st.text_area("Paste Job Description Here:", height=250)

# 4. Prediction Logic
if st.button("Analyze Job Posting"):
    if job_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Preprocess input (matches the training step)
        transformed_text = vectorizer.transform([job_text.lower()])
        
        # Predict
        prediction = model.predict(transformed_text)[0]
        probabilities = model.predict_proba(transformed_text)[0]
        
        # Display Results
        st.divider()
        
        # Class 1 = Fake, Class 0 = Real
        if prediction == 1:
            st.error("🚨 WARNING: This job is likely FAKE!")
            confidence = probabilities[1] * 100
            st.metric(label="Fraud Probability", value=f"{confidence:.2f}%")
            
            st.info("⚠️ Why? The model detected patterns commonly found in scam postings (e.g., vague requirements, suspicious keywords).")
        else:
            st.success("✅ SAFE: This appears to be a LEGITIMATE job.")
            confidence = probabilities[0] * 100
            st.metric(label="Legitimacy Score", value=f"{confidence:.2f}%")
            #To run the site type into terminal: streamlit run app.py