import pandas as pd

def handleGunViolence():
    raw_gun_violence_df = pd.read_csv("./datasets/gun-violence-data_01-2013_03-2018.csv")
    
    gun_violence_df = pd.DataFrame()

    gun_violence_df["State"] = raw_gun_violence_df["state"]
    gun_violence_df["Date"] = raw_gun_violence_df["date"]
    gun_violence_df["Year"] = raw_gun_violence_df["date"].str.split("-").str.get(0)
    
    gun_violence_df["Year"] = gun_violence_df["Year"].astype("int")

    gun_violence_df.to_csv("./clean_datasets/gun_violence.csv", index=False)

    return gun_violence_df

def handleStateCrime():
    state_crime = pd.read_csv("./datasets/state_crime.csv")
    state_crime["Year"] = state_crime["Year"].astype("int")
    state_crime = state_crime.loc[state_crime["Year"] >= 2013]
    state_crime = state_crime.loc[state_crime["Year"] <= 2018]

    state_crime.to_csv("./clean_datasets/state_crime.csv", index=False)

    return state_crime
    

def joinDataset():
    
    gun_violence_df = handleGunViolence()
    state_crime_df = handleStateCrime()

    joined_dataset_df = gun_violence_df.merge(state_crime_df, on=["State","Year"])

    joined_dataset_df.to_csv("./clean_datasets/gv_sc_joined.csv", index=False)

    print(joined_dataset_df.head())


def main():
    joinDataset()

main()