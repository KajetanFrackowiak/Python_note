from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]
wedgeprops = {'linewidth': 1, 'edgecolor': 'black', 'linestyle': ':'}
plt.pie(slices, labels=labels, explode=explode, wedgeprops=wedgeprops, shadow=True, startangle=90, autopct='%1.1f%%')

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
