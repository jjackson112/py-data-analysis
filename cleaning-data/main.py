import json
import re
# .mw-parser-output .nobold{font-weight:normal}(EX)\u00a0 is HTML code from Wikipedia
# clean the data for relevant info - separate conservation status from HTML data in Category

# open the json file and in read mode as text
# data variable contains the json.load() with text inside to create a JSON object
with open("data.json", "r") as text:
    data = json.load(text)

# create for loop to look through data variable
# use item variable and ["Category"] as key - write a regular expression
for item in data:
    item["Category"] = re.compile("[\.(]").split(item["Category"])[0]

print(data)