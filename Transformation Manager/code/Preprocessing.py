import pandas as pd
from pathlib import Path


# Diamond Princess
# Grand Princess
# Repatriated Travellers
# Unknown


def main():
    confirmed_df = pd.read_csv(
        "C:/Users/radha/PycharmProjects/covid-analysis/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
    deaths_df = pd.read_csv(
        "C:/Users/radha/PycharmProjects/covid-analysis/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
    recovered_df = pd.read_csv(
        "C:/Users/radha/PycharmProjects/covid-analysis/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")

    # print(Path.cwd())
    # print(confirmed_df.isna().sum())
    # print(confirmed_df['Province/State'])

    confirmed_df = removeNonNumericRows(confirmed_df)
    print("---------------------------------")
    deaths_df = removeNonNumericRows(deaths_df)
    print("---------------------------------")
    recovered_df = removeNonNumericRows(recovered_df)

    # to fill the missing data
    confirmed_df.loc[confirmed_df["Lat"] == 52.1326, 'Province/State'] = 'Wellington'
    confirmed_df.loc[confirmed_df["Lat"] == -40.9006, 'Province/State'] = 'Soest'
    deaths_df.loc[deaths_df["Lat"] == 52.1326, 'Province/State'] = 'Wellington'
    deaths_df.loc[deaths_df["Lat"] == -40.9006, 'Province/State'] = 'Soest'
    recovered_df.loc[recovered_df["Lat"] == 52.1326, 'Province/State'] = 'Wellington'
    recovered_df.loc[recovered_df["Lat"] == -40.9006, 'Province/State'] = 'Soest'

    # To write cleaned and added value to respective csv files
    confirmed_df.to_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_confirmed_global_cleaned.csv')
    deaths_df.to_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_deaths_global_cleaned.csv')
    recovered_df.to_csv(
        'C:/Users/radha/PycharmProjects/covid-analysis/Transformation Manager/Resources/CSV/time_series_covid19_recovered_global_cleaned.csv')


# To remove bad data that is related to no state at all so there is missing latitude value
def removeNonNumericRows(raw_csv):
    # To filter that out when Lat is 0 drop that raw via loc
    raw_csv = raw_csv.loc[raw_csv["Lat"] != 0]
    # To filter that out when Lat is NaN drop that raw via loc
    raw_csv = raw_csv.loc[raw_csv["Lat"].notnull()]

    return raw_csv
    # listOfRowsToDrop=["Diamond Princess","Grand Princess","Repatriated Travellers","Unknown"]
    # raw_csv.drop(listOfRowsToDrop,inplace=True)


if __name__ == "__main__":
    main()
