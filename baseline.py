import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import metrics
from tensorflow.keras import losses
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def linearRegressionY2(x_train, x_test, y2_train, y2_test):
    model = LinearRegression()
    model.fit(x_train, y2_train)
    y2_pred = model.predict(x_test)

    print(y2_test[0:3], y2_pred[0:3])

    mse = mean_squared_error(y2_test, y2_pred)

    # shit result, dont use linear regression for time series?
    # maybe its because it is unix?
    # read about time series

    return mse

def stateClassificationY1(x, y1, n_y1):
    model = tf.keras.Sequential([
        layers.Dense(128, activation="relu"),
        layers.Dense(n_y1)
    ])

    model.compile(
        optimizer="adam",
        loss=losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[metrics.SparseCategoricalAccuracy()]
    )
    model.build(x["train"].shape)
    model.summary()
    model.fit(x=x["train"], y=y1["train"], validation_data=(x["val"], y1["val"]), batch_size=32, epochs=50)


    # Epoch 50/50
    # 4494/4494 [==============================] - 8s 2ms/step - loss: 0.0965 - sparse_categorical_accuracy: 0.9933 - val_loss: 0.0910 - val_sparse_categorical_accuracy: 0.9974

def main():
    normalized_dataset = pd.read_csv("./normalized_datasets/normalized_joined.csv")
    n_y1 = normalized_dataset["State"].nunique()
    le = LabelEncoder()

    x = normalized_dataset.iloc[:, 3:].to_numpy()
    y1 = normalized_dataset["State"].to_numpy()
    le.fit(y1)
    y1 = le.transform(y1)
    y2 = normalized_dataset["Date"].to_numpy()

    x_train, x_test, y1_train, y1_test, y2_train, y2_test = train_test_split(
    x, y1, y2, test_size=0.2, random_state=42)

    x_train, x_val, y1_train, y1_val, y2_train, y2_val = train_test_split(
    x_train, y1_train, y2_train, test_size=0.25, random_state=42)

    data = {
        "x":{
            "train": x_train,
            "test": x_test,
            "val": x_val
        },
        "y1":{
            "train": y1_train,
            "test": y1_test,
            "val": y1_val
        },
        "y2":{
            "train": y2_train,
            "test": y2_test,
            "val": y2_val
        },
    }
    
    for k1, v1 in data.items():
        for k2, v2 in v1.items():
            print(f"{k1}_{k2}{v2.shape}")

    stateClassificationY1(data["x"], data["y1"], n_y1)

    # y2_mse = linearRegressionY2(x_train, x_test, y2_train, y2_test)



main()