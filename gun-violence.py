import pandas as pd

def main():
    dataset = pd.read_csv("./clean_datasets/clean_gun_violence.csv")

    print(dataset["State"].value_counts())

main()