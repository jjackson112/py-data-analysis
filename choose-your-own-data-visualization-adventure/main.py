import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("books.csv")

max_rating = data["ratings_count"].max()
# print("Highest rating count:", max_rating) // 5629932
num_pages = data["# num_pages"].max()
#print("Highest number of pages:", num_pages) // 6576

# print(data["language_code"])

# create scatterplot comparing reviews and ratings
# alpha=0.5 is to make points more transparent

sns.scatterplot(x="average_rating", y="# num_pages", size="# num_pages", sizes=(1,5), data=data, alpha=0.5)

plt.xlabel("Average Rating")
plt.ylabel("Average Book Review")

plt.title("Compare Rating to Review")
plt.savefig("review_rating.png")

