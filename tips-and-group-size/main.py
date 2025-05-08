import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

# get the size of your parties with data_numpy
# select each row with : 
# grab the index position (the 7th column of dataset)
size = data_numpy[:,6]

# pass data_numpy in NumPy array, select each row and grab the index position
# dtype=float makes the array float because the csv data is in a string - data type
# use tips data to perform calculations
tips = np.array(data_numpy[:, 1], dtype=float)

# 0 index position pulls the total_bill column
bills = np.array(data.numpy[:, 0], dtype=float)

tip_percentages = tips/bills