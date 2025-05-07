import matplotlib.pyplot as plt

month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp = [28,32,31,40,45,55,60,65,54,43,34,30]

# plot function
plt.plot(month, temp, color="#7d32a8")

# label the x-axis
plt.xlabel("Month", fontsize=16)

# label the y-axis
plt.ylabel("Temp in Fahrenheit", fontsize=16)

# give chart a name
plt.title("Average Temperatures for 2018 in North Pole, Alaska")

# how to save chart
plt.savefig("north_pole_temps.png")