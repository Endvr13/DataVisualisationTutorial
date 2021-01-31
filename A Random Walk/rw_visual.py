import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
    # Make a random walk
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(20, 12), dpi=82)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c='red', lw=1)

    # Emphasise first and last points
    ax.plot(0, 0)
    ax.plot(rw.x_values[-1], rw.y_values[-1])

    # Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
