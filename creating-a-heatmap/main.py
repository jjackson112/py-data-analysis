import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csvfile:
    tips = pd.read_csv(csvfile, delimiter=",")

# many duplicated values in tips.csv - pivot_table() will fix
tips_pivoted = tips.pivot_table(
    values = "tip",
    index = ["size"], # y axis
    columns = ["time"] # x axis
    )
# annot set to true means the values will appear inside the boxes
fig = sns.heatmap(tips_pivoted, annot=True, cmap="coolwarm")

# control y axes values - organize it to look better
# or set to (6,0) to have higher values at the bottom
fig.set_ylim(0,5)

plt.xlabel("Time")
plt.ylabel("Size")
plt.title("Average Tip Based on Time and Party Size")
plt.savefig("Show_tips.png")