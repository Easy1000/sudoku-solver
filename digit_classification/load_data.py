import os
from typing import Tuple
import cv2
import numpy as np

digits_directory = os.path.expanduser("./dataset/digits")
data = os.listdir(digits_directory)
data_classes = len(data)


def load_dataset() -> Tuple[np.ndarray, np.ndarray]:
    data_X = []
    data_y = []
    for i in range(0, data_classes):
        data_list = os.listdir(digits_directory + "/" + str(i))
        for j in data_list:
            pic = cv2.imread(digits_directory + "/" + str(i) + "/" + j)
            pic = cv2.resize(pic, (32, 32))
            data_X.append(pic)
            data_y.append(i)

    if len(data_X) == len(data_y):
        print("Total Dataponits = ", len(data_X))

    data_X = np.array(data_X)
    data_y = np.array(data_y)

    return data_X, data_y
