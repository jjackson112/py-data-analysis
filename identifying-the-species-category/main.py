import requests
from bs4 import BeautifulSoup

def get_soup(url):
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  soup = get_soup(url)
  data = {}
  categories = soup.find_all("dl")
  #ADD CODE - select and extract category animals here
  for category in categories:
    category_name = category.find("dt").get_text()
    category_animals = category.find_all("a")
  # add a key-value pair to specify the data extracted from the data dictionary
  # data[category_name] equals the dictionary value
    data[category_name] = category_animals
  # Return the data here
  return data

category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")

print(category_data)
