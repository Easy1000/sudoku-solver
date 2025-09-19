import cv2


def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 6)
    threshold = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    return threshold
