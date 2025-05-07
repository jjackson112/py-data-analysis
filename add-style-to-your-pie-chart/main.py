import matplotlib.pyplot as plt

snack_scores = [80,45,34]

slice_labels = ["Chocolate", "Cheese", "Pickles"]

colors = ["#ffff00", "#dcdcdc", "#808080"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)

plt.title("Snack Scores", fontsize=22)

plt.savefig("snack_scores.png")