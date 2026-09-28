import joblib
import numpy as np
from pathlib import Path


MODEL_PATH = Path(__file__).resolve().parent.parent / "model.pkl"

model = joblib.load(MODEL_PATH)


def predict(features):
    """
    Generate a house value prediction.

    Parameters
    ----------
    features : list
        [MedInc, HouseAge, AveRooms, AveBedrms,
         Population, AveOccup, Latitude, Longitude]

    Returns
    -------
    float
        Predicted median house value in units of $100,000.
    """

    X = np.array([features])

    prediction = model.predict(X)

    return float(prediction[0])