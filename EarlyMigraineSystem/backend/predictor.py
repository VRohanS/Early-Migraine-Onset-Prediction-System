import pickle
import pandas as pd

model = pickle.load(open("backend/model.pkl", "rb"))

def predict(photophobia, phonophobia, typing_speed):
    data = pd.DataFrame([{
        'photophobia': photophobia,
        'phonophobia': phonophobia,
        'Nausea': 0,
        'Vomit': 0,
        'Intensity': 0,
        'Frequency': 0,
        'typing_speed': typing_speed
    }])

    result = model.predict(data)[0]
    return "HIGH RISK" if result == 1 else "NO RISK"