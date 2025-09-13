from typing import Tuple
import numpy as np
from sklearn.model_selection import train_test_split


def split_dataset(
    data_X: np.ndarray, data_y: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    train_X, test_X, train_y, test_y = train_test_split(data_X, data_y, test_size=0.05)
    train_X, valid_X, train_y, valid_y = train_test_split(
        train_X, train_y, test_size=0.2
    )
    print("Training Set Shape = ", train_X.shape)
    print("Validation Set Shape = ", valid_X.shape)
    print("Test Set Shape = ", test_X.shape)

    return train_X, train_y, test_X, test_y, valid_X, valid_y
