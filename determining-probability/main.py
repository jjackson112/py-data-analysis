import csv
import numpy as np
import matplotlib.pyplot as plt

with open("titanic.csv", "r") as file:
    data = csv.reader(file, delimiter=",")
    headers = next(data)
    data = list(data)
    data = np.array(data)

survived = np.array(data[:, [0]], dtype=int).flatten()
fare = np.array(data[:, [7]], dtype=float).flatten()

fare_survived = []
fare_not_survived = []

for index in range(0, len(fare)):
  if survived[index] == 1:
      fare_survived.append(fare[index])
  else:
      fare_not_survived.append(fare[index])

# print(f"The average fare of those who survived was: ${round(np.mean(fare_survived), 2)}")
# print(f"The average fare of those who did not survive was: ${round(np.mean(fare_not_survived), 2)}")

# print(f"The median fare of those who survived was: ${round(np.median(fare_survived), 2)}")
# print(f"The median fare of those who did not survive was: ${round(np.median(fare_not_survived), 2)}")

# use range() to add bins - 15
# start at 0 and no passenger paid more than $240
bins = range(0,240,15)

# alpha value determines the transparency of the bars
plt.hist(fare_not_survived, bins, histtype="bar", color="red", alpha=0.5)
plt.hist(fare_survived, bins, histtype="bar", color="orange", alpha=0.5)

# no one paid more than $240 and the # of people who died don't exceed 360
plt.xticks(range(0, 240, 20))
plt.yticks(range(0, 360,25))

plt.xlabel("Fare")
plt.ylabel("Passengers")

plt.title("Summarizing the Titanic Survival Data")
# Add a legend - color guide
plt.gca().legend(("Did Not Survive", "Survived"))

plt.savefig("determining_probability.png")

