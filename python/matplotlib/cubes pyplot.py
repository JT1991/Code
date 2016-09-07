import matplotlib.pyplot as plt

#create list of values 1 through 1000
x_values = list(range(1, 5001))
#list comprehension generates y-values, looping through x_values and squaring each number
y_values = [x**3 for x in x_values]


plt.scatter(x_values, y_values, s=40, edgecolor='none')

#Set chart title and labels
plt.title("Cube Numbers" , fontsize=24)
plt.xlabel("X Axis", fontsize=14)
plt.ylabel("Y Axis", fontsize=14)


#Set range for each axis
plt.axis([0, 5001, 0, 125000000000])
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')

