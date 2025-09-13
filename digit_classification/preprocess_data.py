from typing import Tuple
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
from .load_data import data_classes
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def prep_image(img: np.ndarray) -> np.ndarray:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img


def preprocess_dataset(
    train_X: np.ndarray,
    test_X: np.ndarray,
    valid_X: np.ndarray,
    train_y: np.ndarray,
    test_y: np.ndarray,
    valid_y: np.ndarray,
) -> Tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    ImageDataGenerator,
]:
    train_X = np.array(list(map(prep_image, train_X)))
    test_X = np.array(list(map(prep_image, test_X)))
    valid_X = np.array(list(map(prep_image, valid_X)))

    train_X = train_X.reshape(train_X.shape[0], train_X.shape[1], train_X.shape[2], 1)
    test_X = test_X.reshape(test_X.shape[0], test_X.shape[1], test_X.shape[2], 1)
    valid_X = valid_X.reshape(valid_X.shape[0], valid_X.shape[1], valid_X.shape[2], 1)

    train_y = to_categorical(train_y, data_classes)
    test_y = to_categorical(test_y, data_classes)
    valid_y = to_categorical(valid_y, data_classes)

    datagen = ImageDataGenerator(
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.2,
        shear_range=0.1,
        rotation_range=10,
    )
    datagen.fit(train_X)

    return train_X, test_X, valid_X, train_y, test_y, valid_y, datagen
