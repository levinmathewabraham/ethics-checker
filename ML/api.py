from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Load model and vectorizer
model = joblib.load('bias_detector_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ethics-checker-frontend.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    text: str

@app.post('/analyze_bias')
def analyze_bias(prompt: Prompt):
    text_vector = vectorizer.transform([prompt.text])
    prediction = model.predict(text_vector)
    label = 'biased' if prediction[0] == 1 else 'unbiased'
    return {"text": prompt.text, "bias_label": label}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
