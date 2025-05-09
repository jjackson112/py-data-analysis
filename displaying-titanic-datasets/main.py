import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# open the titanic.csv file
dataframe = pd.read_csv("titanic.csv")
# add a second variable to make the scatterplot legend clearer 
# 0 and 1 replace the survived and the not survived
dataframe = dataframe.replace({"Survived" : {0: "Did Not Survive", 1 : "Survived"}})

# Build the scatterplot 
# you'll see a different color when a passenger survived or not with the hue argument
# data=dataframe because this variable holds the data from titanic.csv
sns.scatterplot(x="Age", y="Fare", hue="Survived", data=dataframe)

plt.xlabel("Passenger Age")
plt.ylabel("Passenger Fare")

plt.title("Titanic Survivors")
plt.savefig("titanic_survivors.png")