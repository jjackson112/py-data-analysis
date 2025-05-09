import requests
import pandas as pd


# Standardizes currency to USD values so that we can better compare results
def format_currency(dataset):
  url = "https://api.exchangerate-api.com/v4/latest/USD"

  # Requests data from API
  response = requests.get(url)
  data = response.json()

  def convert_currency(row):
    rate = data["rates"][row["Unit Code"]]
    return row["Value"] / rate

  for index, row in dataset.iterrows():
    dataset.at[index, "Unit Code"] = "USD"
    dataset.at[index, "Value"] = convert_currency(row)
  return dataset


# ADD CODE: Pandas dataframes
wage = pd.read_csv("wage.csv", delimiter=",")
print(wage)
happiness = pd.read_csv("happiness.csv", delimiter=",")
print(happiness)

wage_usd = format_currency(wage)
print(wage_usd)

wage_and_happiness = wage.merge(happiness)
print(wage_and_happiness)

# group merged wage_and_happiness with groupby()
wage_and_happiness_by_country = (wage_and_happiness.groupby("Country").sum())

# calculate the mean for the Value series in the dataframe
wage_average_per_country = wage_and_happiness["Value"].mean()

happiness_average_per_country = wage_and_happiness_by_country["Happiness score"].mean()

# Pull 10 countries with the highest average wages
print(f"Countries with largest average wages: ", wage_average_per_country.nlargest(10))

# Pull 10 countries with the smallest average wages
print(f"Countries with the smallese average wages: ", wage_average_per_country.nsmallest(10))

# Pull 10 countries with the highest happiness values 
print(f"Countries with the highest happiness levels: ", happiness_average_per_country.nlargest(10))

# Pull 10 countries with the lowest happiness values 
print(f"Countries with the lowest happiness levels: ", happiness_average_per_country.nsmallest(10))