import re
import json
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

with open("data.json", "r") as text:
    data = json.load(text)

for item in data:
    # Use a more flexible regex to split by space or dot (or other characters if needed)
    # The r in r"[\s.]" creates a raw string, which is good practice for regex
    item["Category"] = re.compile(r"[\s.]").split(item["Category"])[0]

# mosaic plot will show data from these 3 classes
classes = ["Mammalia", "Aves", "Reptilia"]
# will show only these conservation statuses
statuses = ["Endangered", "Critically endangered", "Vulnerable"]

mosaic_data = []

# will only extract data from those classes and conservation statuses
# search for values of each item with a specific class key and category key
for item in data:
    if item["Animal Class"] in classes and item["Category"] in statuses:
        mosaic_data.append(item)

properties = {
    "Endangered": {"color": "#facdb6"},
    "Critically endangered": {"color": "#c5cade"},
    "Vulnerable": {"color": "#a8dbd2"}
}

plt.rc("font", size=8)

# create a dataframe
mosaic_dataframe = pd.DataFrame(mosaic_data)

# Create the mosaic plot
fig = mosaic(mosaic_dataframe, ["Category", "Animal Class"], title="Conservation Status by Animal Class", gap=[0.02, 0.02], axes_label=True, properties=lambda x: properties[x[0]])

plt.savefig("mosaic.png")