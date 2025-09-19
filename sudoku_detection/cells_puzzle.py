import cv2
import numpy as np
from PIL import Image


def splitcells(img):
    rows = np.vsplit(img, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            boxes.append(box)
    return boxes


def crop_cells(cells):
    cells_cropped = []
    for image in cells:
        img = np.array(image)
        img = img[4:46, 6:46]
        img = Image.fromarray(img)
        cells_cropped.append(img)

    return cells_cropped


def read_cells(cell, model):
    result = []
    for image in cell:
        # preprocess the image as it was in the model
        img = np.asarray(image)
        img = img[4 : img.shape[0] - 4, 4 : img.shape[1] - 4]
        img = cv2.resize(img, (32, 32))
        img = img / 255
        img = img.reshape(1, 32, 32, 1)

        # getting predictions and setting the values if probabilities are above 65%
        predictions = model.predict(img)
        classIndex = np.argmax(predictions, axis=-1)[0]
        probabilityValue = np.amax(predictions)

        if probabilityValue > 0.65:
            result.append(classIndex)
        else:
            result.append(0)
    result = np.asarray(result)
    return result
