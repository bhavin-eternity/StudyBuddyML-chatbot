import json
import pickle
import os
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

patterns = []
tags = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Train SVM model
model = LinearSVC()
model.fit(X, tags)

print("Training complete!")

# ----------- FIX: ALWAYS create the models folder ------------
models_dir = "models"
os.makedirs(models_dir, exist_ok=True)

# Save model + vectorizer
model_path = os.path.join(models_dir, "svm_model.pkl")
vec_path = os.path.join(models_dir, "vectorizer.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(vec_path, "wb") as f:
    pickle.dump(vectorizer, f)

print(f"Model saved to {model_path}")
print(f"Vectorizer saved to {vec_path}")
