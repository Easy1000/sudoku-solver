import os
import sys

from tensorflow.keras.models import load_model


def get_model_path(model_path: str):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, model_path)
    return os.path.join(os.path.abspath("."), model_path)


def get_digit_classification_model():
    model_path = get_model_path("digit_classification_model.keras")
    model = load_model(model_path)

    return model
