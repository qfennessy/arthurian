import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def generate_pattern():
    """
    Generates a grid of black shapes, alternating between squares and diamonds, with random rotations.
    """
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Grid size
    rows, cols = 20, 20
    cell_size = 0.5

    # Draw shapes in grid
    for i in range(rows):
        for j in range(cols):
            # Randomly choose rotation (0, 90, 180, 270 degrees)
            angle = random.choice([0, 90, 180, 270])
            x, y = i * cell_size, j * cell_size
            
            # Create a black square or diamond
            shape_type = random.choice(['square', 'diamond'])
            if shape_type == 'square':
                shape = patches.Rectangle((x, y), cell_size, cell_size, angle=angle, color='black')
            else:  # Diamond
                diamond = [
                    (x + cell_size / 2, y),
                    (x + cell_size, y + cell_size / 2),
                    (x + cell_size / 2, y + cell_size),
                    (x, y + cell_size / 2),
                ]
                shape = patches.Polygon(diamond, closed=True, color='black')
            
            ax.add_patch(shape)

    # Display the pattern
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Generate the pattern
generate_pattern()

