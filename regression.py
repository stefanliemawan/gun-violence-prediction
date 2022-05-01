import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def main():
    normalized_dataset = pd.read_csv("./normalized_datasets/normalized_joined.csv")

    le = LabelEncoder()

    x = normalized_dataset.iloc[:, 3:].to_numpy()
    y1 = normalized_dataset["State"].to_numpy()
    le.fit(y1)
    y1 = le.transform(y1)
    y2 = normalized_dataset["Date"].to_numpy()

    print(x,y1,y2)
    

main()