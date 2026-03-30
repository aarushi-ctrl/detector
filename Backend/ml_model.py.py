import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "url_length": [20, 120, 60, 150],
    "dots": [2, 5, 3, 6],
    "hyphens": [0, 3, 1, 4],
    "has_at": [0, 1, 0, 1],
    "login_word": [0, 1, 0, 1],
    "verify_word": [0, 1, 0, 1],
    "https": [1, 0, 1, 0],
    "label": [0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))