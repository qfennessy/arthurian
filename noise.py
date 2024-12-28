import matplotlib.pyplot as plt
import numpy as np
import random


def generate_abstract_diagram(output_file='abstract_art.png'):
    """
    Generates a complex abstract diagram of overlapping polygons and lines.
    
    Args:
        output_file (str): Path to save the output PNG file. Defaults to 'abstract_art.png'.
    """
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.axis('off')

    # Number of shapes
    num_shapes = 200

    for _ in range(num_shapes):
        # Random center
        center_x, center_y = random.uniform(-100, 100), random.uniform(-100, 100)
        # Random number of vertices
        num_vertices = random.randint(3, 10)
        # Generate angles for vertices
        angles = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        # Random radius
        radius = random.uniform(5, 20)
        # Compute polygon vertices
        x = center_x + radius * np.cos(angles)
        y = center_y + radius * np.sin(angles)
        # Add random connections
        if random.random() < 0.5:
            ax.plot([center_x] + x.tolist() + [center_x], [center_y] + y.tolist() + [center_y], 'k-', linewidth=0.5)
        else:
            ax.plot(x, y, 'k-', linewidth=0.5)

    # Add random lines
    for _ in range(150):
        x1, y1 = random.uniform(-100, 100), random.uniform(-100, 100)
        x2, y2 = random.uniform(-100, 100), random.uniform(-100, 100)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=0.3)

    # Save the plot to file
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()


# Run the function
generate_abstract_diagram('abstract_art.png')
