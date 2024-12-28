import matplotlib.pyplot as plt
import numpy as np
import random

def generate_layered_triangles(output_file: str, background_color: str = "#000000", num_layers: int = 5, triangles_per_layer: int = 200):
    """
    Generates layered semi-transparent triangles to create a dynamic, textured abstract design.

    Parameters:
        output_file (str): The file name to save the output image.
        background_color (str): The background color of the image (default is black).
        num_layers (int): The number of layers of triangles.
        triangles_per_layer (int): The number of triangles per layer.
    """
    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.axis('off')
    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)

    # Define color palettes for layering
    color_palettes = [
        ['#FF5733', '#FF8D1A', '#FFC300', '#C70039', '#900C3F'],  # Warm tones
        ['#33A1FF', '#1A8DFF', '#4DC3FF', '#00539C', '#003F5C'],  # Cool tones
        ['#00FFAB', '#00FFC6', '#00FFD8', '#00E6B8', '#00BFA5'],  # Green tones
        ['#FFC0CB', '#FF69B4', '#FF1493', '#FF7F50', '#FFDAB9'],  # Pink tones
        ['#FFD700', '#FFA500', '#FF8C00', '#FF6347', '#FF4500'],  # Bright warm tones
    ]

    for layer in range(num_layers):
        color_palette = random.choice(color_palettes)  # Randomly choose a palette for each layer
        for _ in range(triangles_per_layer):
            # Randomize the position, size, and rotation of each triangle
            x = random.uniform(-100, 100)
            y = random.uniform(-100, 100)
            size = random.uniform(5, 30)
            angle = random.uniform(0, 360)

            # Generate vertices for an equilateral triangle
            vertices = np.array([
                [0, 0],
                [size, 0],
                [size / 2, np.sqrt(3) * size / 2]
            ])

            # Rotate the triangle
            rotation_matrix = np.array([
                [np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
                [np.sin(np.radians(angle)), np.cos(np.radians(angle))]
            ])
            rotated_vertices = np.dot(vertices - [size / 2, size / (2 * np.sqrt(3))], rotation_matrix) + [x, y]

            # Randomly choose a color from the palette and apply transparency
            color = random.choice(color_palette)
            alpha = random.uniform(0.2, 0.7)

            # Add the triangle to the plot
            ax.fill(rotated_vertices[:, 0], rotated_vertices[:, 1], color=color, alpha=alpha)

    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=background_color)
    plt.close()

# Example usage
generate_layered_triangles("layered_triangles.png", background_color="#2C2C2C")
