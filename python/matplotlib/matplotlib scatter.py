import matplotlib.pyplot as plt

#Lists for plot points
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

#matplotlib reads one values from each list as it plots each point
plt.scatter(x_values, y_values, s=100)

#Set chart axis and title
plt.title("Scatter Points" , fontsize=24)
plt.xlabel("X Axis", fontsize=14)
plt.ylabel("Y Axis", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
