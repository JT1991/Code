import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

#Loop of random walks
while True:
#Make a random walk and plot the points
    rw = RandomWalk(100000)
    rw.fill_walk()

    #Set size of window
    plt.figure(figsize=(10, 6))

    #Generate list equal to number of points in the walk
    point_numbers = list(range(rw.num_points))
    #use list to set plot point gradient.
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap= plt.cm.Blues,
                edgecolor='none', s=1)
    
    #Emphasise start and end plot points
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    #Remove axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = raw_input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    
    
