import json
import pickle
import os
import random

MODEL_PATH = os.path.join("models", "svm_model.pkl")
VEC_PATH = os.path.join("models", "vectorizer.pkl")

# Load model + vectorizer
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VEC_PATH, "rb") as f:
    vectorizer = pickle.load(f)

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# Load intents
intents = json.load(open("intents.json"))

def chatbot(message):
    X = vectorizer.transform([message])
    predicted_tag = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."
