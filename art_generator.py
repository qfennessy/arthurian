#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import CSS4_COLORS

import numpy as np
import random
import argparse


def parse_color(color_arg):
    """
    Parses the color argument and returns a valid matplotlib color.
    Accepts either:
      - CSS4 named colors (e.g., 'blue', 'lemonchiffon')
      - Extended custom colors (e.g., 'lemonyellow', 'grassgreen')
      - RGB values in the format 'r,g,b' (0-255)
    """
    # Extended custom colors dictionary
    custom_colors = {
        'lemonyellow': (255 / 255, 250 / 255, 205 / 255),  # Light yellow
        'grassgreen': (124 / 255, 252 / 255, 0 / 255),     # Greenish-yellow
        'skyblue': (135 / 255, 206 / 255, 235 / 255),      # Light blue
        'coralred': (255 / 255, 127 / 255, 80 / 255),      # Coral
    }

    if ',' in color_arg:
        # Parse as RGB
        try:
            r, g, b = map(int, color_arg.split(','))
            if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                raise ValueError
            return (r / 255, g / 255, b / 255)  # Normalize to 0-1
        except ValueError:
            raise argparse.ArgumentTypeError("RGB color must be in the format r,g,b where r, g, b are integers between 0 and 255.")
    else:
        # Check in CSS4 colors
        if color_arg.lower() in CSS4_COLORS:
            return CSS4_COLORS[color_arg.lower()]
        # Check in custom colors
        if color_arg.lower() in custom_colors:
            return custom_colors[color_arg.lower()]
        raise argparse.ArgumentTypeError(f"Unknown color: {color_arg}. Use RGB (e.g., '255,255,0') or a valid color name.")



def generate_noise(output_file, background_color):
    """
    Generates a complex abstract diagram of overlapping polygons and lines with randomized shades of gray and rotations.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-100, 100)  # Canvas dimensions
    ax.set_ylim(-100, 100)
    ax.axis('off')  # Remove axes for aesthetics
    fig.patch.set_facecolor(background_color)

    # Number of shapes to draw
    num_shapes = random.randint(150, 400)

    for _ in range(num_shapes):
        # Random position for the center of the shape
        center_x, center_y = random.uniform(-100, 100), random.uniform(-100, 100)
        # Random number of sides for the polygon (minimum 4, maximum 9)
        num_vertices = random.randint(4, 9)
        # Generate angles for evenly spaced vertices
        angles = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        # Random radius for the shape
        radius = random.uniform(4, 32)
        # Compute vertices of the polygon
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)

        # Apply a random rotation to the shape
        rotation_angle = random.uniform(0, 2 * np.pi)
        rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                     [np.sin(rotation_angle), np.cos(rotation_angle)]])
        rotated_vertices = np.dot(rotation_matrix, np.array([x, y]))
        x_rotated = rotated_vertices[0] + center_x
        y_rotated = rotated_vertices[1] + center_y

        # Randomize shade of gray for the shape
        gray_shade = random.uniform(0.4, 1.0)
        color = (gray_shade, gray_shade, gray_shade)

        # Plot the shape with or without a connection to its center
        if random.random() < 0.95:
            ax.plot([center_x] + x_rotated.tolist() + [center_x],
                    [center_y] + y_rotated.tolist() + [center_y],
                    color=color, linewidth=1.2)
        else:
            ax.plot(x_rotated, y_rotated, color=color, linewidth=0.8)

    # Draw additional random lines for texture
    for _ in range(150):
        x1, y1 = random.uniform(-100, 100), random.uniform(-100, 100)
        x2, y2 = random.uniform(-100, 100), random.uniform(-100, 100)
        # Randomize line color (shades of gray)
        gray_shade = random.uniform(0, 1)
        color = (gray_shade, gray_shade, gray_shade)
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=0.3)

    # Save the figure with the specified background color
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=background_color)
    plt.close()


def generate_radial(output_file, background_color):
    """
    Generates a colorful radial diagram with evenly spaced lines radiating outward in all directions,
    with varied colors and random lengths.
    """
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    fig.patch.set_facecolor(background_color)

    # Number of radial lines
    num_lines = 500

    # Generate evenly spaced angles
    angles = np.linspace(0, 2 * np.pi, num_lines, endpoint=False)

    for angle in angles:
        # Random line length for variation
        length = random.uniform(0.4, 1.0)
        # Random color for the line
        color = (random.random(), random.random(), random.random())
        # Draw the line from the center outward
        ax.plot([angle, angle], [0, length], color=color, lw=1)

    # Remove grid, ticks, and spines for a clean look
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)
    ax.set_facecolor(background_color)

    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=background_color)
    plt.close()

def generate_squares(output_file, background_color):
    """
    Generates a grid of shapes with varying sizes, colors, and rotations, creating a dynamic mosaic pattern.
    Introduces randomized empty spaces for a more balanced layout.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor(background_color)
    fig.patch.set_facecolor(background_color)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.axis('off')

    # Grid size
    rows, cols = 15, 15
    base_size = 0.8  # Base size for the shapes

    # Color palettes
    color_palettes = [
        ['#FF5733', '#33FF57', '#3357FF', '#FFC300', '#900C3F'],
        ['#FFD700', '#0057E7', '#FF4F81', '#00C49F', '#7B2CBF'],
        ['#2E86C1', '#EC7063', '#F4D03F', '#58D68D', '#AF7AC5'],
        ['#1F618D', '#F1C40F', '#E74C3C', '#239B56', '#884EA0'],
        ['#DFFF00', '#FF1493', '#40E0D0', '#800080', '#FFD700'],
        ['#8E44AD', '#3498DB', '#F39C12', '#2ECC71', '#E74C3C'],
    ]

    # Randomly select a color palette
    colors = random.choice(color_palettes)

    for i in range(rows):
        for j in range(cols):
            # Randomly skip some cells to create empty spaces
            if random.random() < 0.3:  # Uniform randomization for skipping
                continue

            # Adjust size based on position for variety
            size_factor = 0.5 + 0.5 * np.sin(i / 3) * np.cos(j / 3)
            cell_size = base_size * size_factor
            # Add randomness to the position
            x = i * (10 / rows) + random.uniform(-0.5, 0.5)
            y = j * (10 / cols) + random.uniform(-0.5, 0.5)
            # Randomize rotation angle
            angle = (i * j) % 90 + random.uniform(-10, 10)
            # Randomly select a shape and color
            shape_type = random.choice(['square', 'diamond', 'circle'])
            color = random.choice(colors)

            # Draw the selected shape
            if shape_type == 'square':
                rect = patches.Rectangle(
                    (x - cell_size / 2, y - cell_size / 2),
                    cell_size, cell_size,
                    angle=angle,
                    facecolor=color,
                    alpha=0.7
                )
                ax.add_patch(rect)
            elif shape_type == 'diamond':
                diamond = patches.RegularPolygon(
                    (x, y),
                    4,
                    radius=cell_size / np.sqrt(2),
                    orientation=np.radians(angle),
                    facecolor=color,
                    alpha=0.7
                )
                ax.add_patch(diamond)
            else:
                circle = patches.Circle(
                    (x, y),
                    radius=cell_size / 2,
                    facecolor=color,
                    alpha=0.7
                )
                ax.add_patch(circle)

    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=background_color)
    plt.close()

def generate_irregular_polygons(output_file, background_color):
    """
    Generates a grid of irregular polygons with varying sizes, colors, and rotations,
    creating a dynamic and organic mosaic pattern.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor(background_color)
    fig.patch.set_facecolor(background_color)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.axis('off')

    # Grid size: Defines the number of rows and columns
    rows, cols = 15, 15
    base_size = 0.8  # Base size for the shapes

    # Define multiple contrasting color palettes
    color_palettes = [
        ['#FF5733', '#33FF57', '#3357FF', '#FFC300', '#900C3F'],
        ['#FFD700', '#0057E7', '#FF4F81', '#00C49F', '#7B2CBF'],
        ['#2E86C1', '#EC7063', '#F4D03F', '#58D68D', '#AF7AC5'],
        ['#1F618D', '#F1C40F', '#E74C3C', '#239B56', '#884EA0'],
        ['#DFFF00', '#FF1493', '#40E0D0', '#800080', '#FFD700'],
        ['#8E44AD', '#3498DB', '#F39C12', '#2ECC71', '#E74C3C'],
    ]

    # Randomly select a color palette
    colors = random.choice(color_palettes)

    for i in range(rows):
        for j in range(cols):
            # Randomly skip some cells to create empty spaces
            if random.random() < 0.3:  # 30% chance to skip a cell
                continue

            # Adjust size based on position for variety
            size_factor = 0.5 + 0.5 * np.sin(i / 3) * np.cos(j / 3)
            cell_size = base_size * size_factor
            # Add randomness to the position
            x_center = i * (10 / rows) + random.uniform(-0.5, 0.5)
            y_center = j * (10 / cols) + random.uniform(-0.5, 0.5)
            # Randomize the number of sides (3 to 8)
            num_vertices = random.randint(3, 8)
            # Generate random angles for the vertices
            angles = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
            # Add some noise to the radius of each vertex
            radii = [cell_size * (0.7 + random.uniform(-0.3, 0.3)) for _ in range(num_vertices)]
            # Compute vertices
            x_vertices = [x_center + radii[k] * np.cos(angle) for k, angle in enumerate(angles)]
            y_vertices = [y_center + radii[k] * np.sin(angle) for k, angle in enumerate(angles)]

            # Randomly select a color
            color = random.choice(colors)

            # Draw the irregular polygon
            polygon = patches.Polygon(
                xy=list(zip(x_vertices, y_vertices)),
                closed=True,
                facecolor=color,
                edgecolor='white',  # Optional white outline for contrast
                alpha=0.7
            )
            ax.add_patch(polygon)

    # Save the figure with the specified background color
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor=background_color)
    plt.close()



def normalize_color_to_255(color):
    """
    Converts a color in 0-1 range back to 0-255 range.
    If the input is a named color, it is returned as is.
    """
    if isinstance(color, tuple):
        # Convert each channel from 0-1 to 0-255
        return tuple(int(c * 255) for c in color)
    return color  # Return named colors as is


def main():
    parser = argparse.ArgumentParser(description='Generate various types of artistic patterns')
    parser.add_argument('style', choices=['noise', 'radial', 'squares', 'polygons'],
                        help='The style of art to generate')
    parser.add_argument('-o', '--output', default='art.png',
                        help='Output file name (default: art.png)')
    parser.add_argument('--background', '--bg', type=parse_color, default='black',
                        help='Background color (e.g., "blue" or "255,255,255"). Default is "black".')

    args = parser.parse_args()

    # Map of style names to generator functions
    generators = {
        'noise': generate_noise,
        'radial': generate_radial,
        'squares': generate_squares,
        'polygons': generate_irregular_polygons
    }

    # Convert args.color back to 0-255 for passing to the generator
    converted_background_color = normalize_color_to_255(args.background)
    print(f"Generating {args.style} art with background color {converted_background_color}...")
    generators[args.style](args.output, converted_background_color)
    print(f"Art saved to {args.output}")


if __name__ == '__main__':
    main()
