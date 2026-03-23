# 🕵️‍♂️ Multimodal Fake Job Detection System (V3.0)

A Deep Learning-powered web application designed to identify fraudulent recruitment postings in real-time. This project has evolved from traditional Machine Learning baselines to a robust **Multi-Layer Perceptron (MLP)** architecture, achieving high precision to protect job seekers from financial and data theft.

## 🚀 Live Demo
[Access the Streamlit Web App](https://fake-job-detectio-m2ewf6ifneqe4zpwssfaxd.streamlit.app/)

---

## 🏗️ System Architecture
The V3.0 system utilizes a Deep Neural Network to capture complex linguistic patterns in job descriptions that traditional keyword-based filters miss.

### Functional Block Diagram
![Functional Block Diagram](DLFunctioinal_Block_Diagram.jpg)

### Technical Architecture
The model consists of a Multi-Layer Perceptron with two hidden layers (100/50 nodes) utilizing **ReLU** activation and a **Sigmoid** output layer for binary classification.
![System Architecture](DLArchitectureDiagram.png)

---

## 🛠️ Tech Stack
* **Core Language:** Python
* **Frontend:** Streamlit (Real-time inference engine)
* **ML Model:** Deep Neural Network / Multi-Layer Perceptron (MLP)
* **Data Processing:** Pandas, NumPy, NLTK & Regex
* **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency) capped at **5,000 features**
* **Optimization:** Adam Optimizer
* **Serialization:** Joblib

---

## 📊 Performance (V3.0 MLP)
The transition to Deep Learning has significantly improved the system's ability to minimize "false alarms" (False Positives) while maintaining high overall accuracy.

| Metric | Value |
| :--- | :--- |
| **Accuracy** | **98.43%** |
| **Precision (Fake)** | **89%** |
| **Recall (Fake)** | **77%** |
| **F1-Score** | **83%** |

---

## 💻 How to Run Locally

```bash
# 1. Clone the repository
git clone [https://github.com/RajeevRayagada/fake-job-detection.git](https://github.com/RajeevRayagada/fake-job-detection.git)
cd fake-job-detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py
🔮 Future Scope
Contextual AI Upgrade: Transitioning from MLP to Transformer-based models (e.g., BERT) for deeper semantic understanding.

Multimodal Metadata Verification: Expanding the model to verify non-text features like company domain age, logo authenticity, and email domain validation.

Browser Extension: Deploying as a real-time plug-in to automatically scan job boards like LinkedIn and Indeed.

👨‍💻 Team & Supervision
Team Members: Syed Junaid Bukhari, Rajeev Patnaik Rayagada, Jayadev Nukala

Supervisor: Dr. G. Deena (Assistant Professor, CSE-AIML)

Institution: SRM Institute of Science and Technology
