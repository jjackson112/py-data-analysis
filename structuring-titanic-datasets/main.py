import csv
import numpy as np

with open("titanic1.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data1 = np.array(data_list)

with open("titanic2.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  titanic_data2 = np.array(data_list)

combined_data = np.concatenate((titanic_data1, titanic_data2), axis=0)

print(combined_data.shape)
print(combined_data.ndim)

# use tolist() to transform combined_data NumPy array back to a regular list 
# after this you should have a list with several little lists - one list for each row of your combined Titantic datasets
listify = combined_data.tolist()

# save the contents of listify as a csv file and turn the list of lists into a string
# Titanic data will be stored here when they're converted into a string
titanic_lists_to_string = []

# for loop - join method converts data to a string
# use append() to add each string of data onto titantic_string, storing each converted list
for titanic_lists in listify:
  titanic_string = (",").join(titanic_lists)
  titanic_lists_to_string.append(titanic_string)
# ("\n") is now used as a delimiter (new line) so each row of data is on one line
complete_titanic = ("\n").join(titanic_lists_to_string)

# write the string to a csv file
# select the headers and data columns to add to csv file
# write the data to the new csv file, adding the string
with open("titanic.csv", "w") as file:
  file.write("Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare\n")
  file.write(complete_titanic)

# if done correctly, you should see a new titanic.csv file 