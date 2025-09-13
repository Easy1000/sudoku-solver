import numpy as np
from tensorflow.keras.layers import (
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    MaxPooling2D,
)
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import load_img, img_to_array


def build_model() -> Sequential:
    model = Sequential()

    model.add(
        (Conv2D(60, (5, 5), input_shape=(32, 32, 1), padding="Same", activation="relu"))
    )
    model.add((Conv2D(60, (5, 5), padding="same", activation="relu")))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add((Conv2D(30, (3, 3), padding="same", activation="relu")))
    model.add((Conv2D(30, (3, 3), padding="same", activation="relu")))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(500, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(10, activation="softmax"))

    model.summary()

    return model


def compile_model(model: Sequential) -> Sequential:
    optimizer = RMSprop(learning_rate=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
    model.compile(
        optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"]
    )

    return model


def fit_model(
    model: Sequential,
    datagen: ImageDataGenerator,
    train_X: np.ndarray,
    train_y: np.ndarray,
    valid_X: np.ndarray,
    valid_y: np.ndarray,
) -> Sequential:
    model.fit(
        datagen.flow(train_X, train_y, batch_size=32),
        epochs=30,
        validation_data=(valid_X, valid_y),
        verbose=2,
        steps_per_epoch=200,
    )

    return model


def model_score(model: Sequential, test_X: np.ndarray, test_y: np.ndarray):
    score = model.evaluate(test_X, test_y, verbose=0)
    print("Test score = ", score[0])
    print("Test accuracy = ", score[1])


def save_model(model: Sequential):
    model.save("digit_classification_model.keras")


def model_predict(image_path: str):
    model = load_model("digit_classification_model.keras")
    img = load_img(image_path, color_mode="grayscale", target_size=(32, 32))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    print("Raw prediction vector:", predictions)
    print("Predicted digit:", predicted_class)
