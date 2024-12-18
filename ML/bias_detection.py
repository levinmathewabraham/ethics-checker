import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Dataset (CrowS-Pairs sample data)
data = {
    'text': [
        'Men are better drivers than women.',
        'Everyone should have equal rights.',
        'She is not as smart as he is.',
        'Cats make great pets.'
    ],
    'bias_label': [1, 0, 1, 0]  # 1 = biased, 0 = unbiased
}
df = pd.DataFrame(data)

# Vectorize Text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['bias_label']

# Train Model
model = MultinomialNB()
model.fit(X, y)

# Save Model and Vectorizer
joblib.dump(model, 'bias_detector_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Bias Detection Model trained and saved!")
