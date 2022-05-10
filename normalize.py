import pandas as pd
from sklearn.preprocessing import Normalizer
from datetime import timedelta

def normalize(features):
    normalizer = Normalizer().fit(features)
    return normalizer.transform(features)

def convertDateToUnix(date_series):
    date_series = pd.to_datetime(date_series)
    return (date_series - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')


def main():
    dataset = pd.read_csv("./clean_datasets/gv_sc_joined.csv")
    dataset["Date"] = convertDateToUnix(dataset["Date"])

    features = dataset.iloc[:, 3:].to_numpy()
    
    normalized_features = normalize(features)

    dataset.iloc[:, 3:] = normalized_features
    dataset.to_csv("./normalized_datasets/gv_sc_joined.csv", index=False)


main()