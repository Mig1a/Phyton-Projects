import pandas as pd
## Loading the data -----------
df = pd.read_csv("C:/Users/mella/OneDrive/Desktop/GMU/IT 209/CrimeReports (1).csv")
headers = ["A", "Code", "Crime_Type", "Date", "Time", "Address", "City", "abb", "Zipcode"]
df.columns = headers

## Most reported Crimetype in city----------

count = df.groupby(['City', "Crime_Type"])["Crime_Type"].value_counts()
most_reported_crime = count.groupby(level=0).idxmax().apply(lambda x: x[1])
new_count = pd.DataFrame(most_reported_crime)
new_count.to_excel("C:/Users/mella/OneDrive/Desktop/GMU/IT 209/Most_reported_Crimetype_in_city.xlsx",
                       index=True)

## crime count by city -----------

count = df[['City', "Crime_Type"]].groupby("City").count().sort_values("Crime_Type", ascending=False)



## Freqently occured incident---------
freq = df.groupby("Crime_Type")["Crime_Type"].count().sort_values(ascending=False)
freq.to_excel("C:/Users/mella/OneDrive/Desktop/GMU/IT 209/Freq_incident.xlsx",
                  index=True)


def categorize_time(hour):
    if 0 <= hour < 6:
        return 'Night'
    elif 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

###  Time trend -----------
df['Hour'] = df['Time'] // 100
df['Time_Category'] = df['Hour'].apply(Report.categorize_time())
trend = df.groupby(["Time_Category", "Crime_Type"])["Crime_Type"].count().sort_values("Crime_Type",ascending=False)
trend.to_excel("C:/Users/mella/OneDrive/Desktop/GMU/IT 209/time_trend.xlsx",index=True)
