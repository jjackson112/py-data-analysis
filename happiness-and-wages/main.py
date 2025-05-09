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
    dataset.at[index,"Unit Code"] = "USD"
    dataset.at[index,"Value"] = convert_currency(row)
  return dataset


# ADD CODE: Pandas dataframes
wage = pd.read_csv("wage.csv", delimiter=",")
happiness = pd.read.csv("happiness.csv", delimiter=",")

print(wage)
print(happiness)

# pass wage dataframe as an argument for format_currency in the wage_usd variable
wage_usd= format_currency(wage)

print(wage_usd)

# merge the dataframes
wage_and_happiness = wage.merge(happiness)

print(wage_and_happiness)