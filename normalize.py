import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer

def normalize(features):
    normalizer = Normalizer().fit(features)
    return normalizer.transform(features)


def main():
    dataset = pd.read_csv("./clean_datasets/clean_joined.csv")
    features = dataset.iloc[:, 3:].to_numpy()
    
    normalized_features = normalize(features)

    dataset.iloc[:, 3:] = normalized_features
    dataset.to_csv("./normalized_datasets/normalized_joined.csv")


main()