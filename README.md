# 🎓 StudyBuddyML  
A lightweight machine-learning powered study assistant chatbot built using **TF-IDF**, **Linear SVM**, and **Streamlit**.

---

## 📌 Overview  
**StudyBuddyML** is a traditional machine-learning chatbot designed to help students with studying, motivation, exam preparation, productivity, and time management.  
It uses **TF-IDF vectorization** and a **Linear Support Vector Machine** classifier to detect user intent and return helpful responses.

This project is ideal for:
- Students learning machine learning  
- Beginners exploring NLP  
- Developers building simple chatbots  
- Portfolio / GitHub showcase projects  

---

## 🚀 Features  
- 🔍 **TF-IDF + Linear SVM** machine-learning model  
- 💬 **Streamlit chat UI**  
- 🧠 20+ study-related intents (motivation, time management, subject help, exam tips, etc.)  
- 📚 Easy-to-edit `intents.json`  
- 🔁 Simple retraining pipeline with `train_svm.py`  
- 🗂 Organized project structure with a dedicated **models/** folder  
- 🆓 Fully open-source under the **MIT License**

---------------------------------------------------------------------------------------------

## 📂 Project Structure  

StudyBuddyML/
│
├── app.py # Streamlit chat interface
├── svm_chatbot.py # Loads model + predicts user intent
├── train_svm.py # Script to train & save SVM model
├── intents.json # Intents, patterns, responses for chatbot
├── README.md # Project documentation
├── LICENSE # MIT Open Source License
│
└── models/
├── svm_model.pkl
└── vectorizer.pkl

------------------------------------------------------------------------------------------------
## 🧠 How It Works  

1. User message → converted into TF-IDF vector  
2. Linear SVM predicts the best-matching **intent tag**  
3. Chatbot selects a random response from `intents.json`  
4. Streamlit displays messages in a clean chat interface  

A simple, fast, and effective ML-based chatbot workflow.

---

## 🛠 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/bhavin-eternity/StudyBuddyML
cd StudyBuddyML
```
```
python -m venv venv
venv\Scripts\activate   # Windows
```

```
pip install -r requirements.txt
```
---------------------------------------------------------------------------------
If you edit or expand intents.json, retrain the model:
python train_svm.py

This produces two files inside models/:
models/svm_model.pkl
models/vectorizer.pkl

---------------------------------------------------------------------------------
💬 Running the Chatbot
```
streamlit run app.py
```
Then open the URL:http://localhost:8501

--------------------------------------------------------------------------------

⭐ Support

If you found this project useful or educational,
please give the repository a ⭐ on GitHub!
It helps others discover it and supports the project.
