import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk(500_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    # figsize=(16,9) is used to set the dimensions of plot window in inches.
    # matplotlib assumes screen resolution is 100 pixels per inch.
    # fig, ax = plt.subplots()
    # fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    fig, ax = plt.subplots(figsize=(16,9))
    # produce a range(0, 5000), point_numbers will then set the color of each point
    # from white to dark blue. edgecolors is set to get rid of black outline around
    # each point.
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    # Emphasize the first and last points
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
