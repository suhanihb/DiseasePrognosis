from django.db import models
import joblib

def load_trained_model():
    try:
        model = joblib.load('../main.pkl')
        return model
    except Exception as e:
        print(f"Error loading the model: {str(e)}")
        return None

model = load_trained_model()