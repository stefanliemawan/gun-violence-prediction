from tokenize import group
import pandas as pd

def main():
    gun_violence_df = pd.read_csv("./clean_datasets/gun_violence.csv")
    gun_violence_df.drop(["Date"], axis=1, inplace=True)

    group_by_year = gun_violence_df.groupby(["Year"])
    group_by_state_year = gun_violence_df.groupby(["State", "Year"])

    crime_chance_series  = group_by_state_year["State"].count() / group_by_year["Year"].count()
    crime_chance_df = crime_chance_series.reset_index()
    crime_chance_df.rename(columns={0 : "Crime.Chance"}, inplace=True)

    crime_chance_df.to_csv("./modified_datasets/crime_chance.csv", index=False)

    state_crime_df = pd.read_csv("./datasets/state_crime.csv")

    state_crime_df = state_crime_df.merge(crime_chance_df, on=["State","Year"])

    state_crime_df.to_csv("./modified_datasets/state_crime_with_chance.csv")

main()
