import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(20, 12), dpi=82)
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.plasma, edgecolors='none', s=1)
    # Emphasise first and last points
    ax.scatter(0, 0, c='midnightblue', edgecolors='black', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='gold', edgecolors='black', s=100)

    # Remove axes

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    elif keep_running == 'y':
        continue
