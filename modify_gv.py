import pandas as pd

def groupByDate():
    gv_df = pd.read_csv("./clean_datasets/gun_violence.csv") 

    grouped_by_date = dict(list(gv_df.groupby(["Date"])))

    dates = []
    states = []

    for key, value in grouped_by_date.items():
        dates.append(key)
        states.append(";".join(value["State"]))

    modified_gv_df = pd.DataFrame({"Dates": dates, "States": states})

    modified_gv_df.to_csv("./modified_datasets/gun_violence.csv", index=False)

def addMissingDates():
    gv_df = pd.read_csv("./modified_datasets/gun_violence.csv")

def main():
    groupByDate()


main()