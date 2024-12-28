import matplotlib.pyplot as plt
import numpy as np
import random

def generate_radial_diagram():
    """
    Generates a colorful radial diagram with lines radiating outward in all directions.
    """
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

    # Number of lines
    num_lines = 500

    # Generate lines
    for _ in range(num_lines):
        # Random angle in radians
        angle = random.uniform(0, 2 * np.pi)

        # Random line length
        length = random.uniform(0.4, 1.0)

        # Random color
        color = (random.random(), random.random(), random.random())

        # Draw the line from center to outer point
        ax.plot([angle, angle], [0, length], color=color, lw=0.8)

    # Hide grid, ticks, and spines
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)

    # Set background color
    ax.set_facecolor('black')

    # Show the plot
    plt.show()

# Run the function
generate_radial_diagram()

