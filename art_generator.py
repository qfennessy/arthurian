#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import argparse

import matplotlib.pyplot as plt
import numpy as np
import random

def generate_noise(output_file):
    """
    Generates a complex abstract diagram of overlapping polygons and lines with randomized shades of gray and rotations.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.axis('off')

    # Number of shapes
    num_shapes = random.randint(150, 400)

    for _ in range(num_shapes):
        # Random center
        center_x, center_y = random.uniform(-100, 100), random.uniform(-100, 100)
        # Random number of vertices
        num_vertices = random.randint(4, 9)
        # Generate angles for vertices
        angles = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
        # Random radius
        radius = random.uniform(4, 32)
        # Compute polygon vertices
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)

        # Apply random rotation
        rotation_angle = random.uniform(0, 2 * np.pi)  # Rotation angle in radians
        rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                     [np.sin(rotation_angle), np.cos(rotation_angle)]])
        rotated_vertices = np.dot(rotation_matrix, np.array([x, y]))
        x_rotated = rotated_vertices[0] + center_x
        y_rotated = rotated_vertices[1] + center_y

        # Random gray shade
        gray_shade = random.uniform(.4, 1.0)
        color = (gray_shade, gray_shade, gray_shade)

        # Add random connections
        if random.random() < 0.95:
            ax.plot([center_x] + x_rotated.tolist() + [center_x],
                    [center_y] + y_rotated.tolist() + [center_y], 
                    color=color, linewidth=1.2)
        else:
            ax.plot(x_rotated, y_rotated, color=color, linewidth=0.8)

    # Add random lines
    for _ in range(150):
        x1, y1 = random.uniform(-100, 100), random.uniform(-100, 100)
        x2, y2 = random.uniform(-100, 100), random.uniform(-100, 100)
        # Random gray shade
        gray_shade = random.uniform(0, 1)
        color = (gray_shade, gray_shade, gray_shade)
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=0.3)

    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()



def generate_radial(output_file):
    """
    Generates a colorful radial diagram with lines radiating outward in all directions.
    """
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

    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='black')
    plt.close()

def generate_squares(output_file):
    """
    Generates a grid of shapes with varying sizes, colors, and rotations creating a dynamic mosaic pattern.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor('black')
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.axis('off')

    # Grid size
    rows, cols = 15, 15
    base_size = 0.8

    # Color palette - modern and vibrant
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD']

    # Draw shapes in grid
    for i in range(rows):
        for j in range(cols):
            # Vary size based on position
            size_factor = 0.5 + 0.5 * np.sin(i/3) * np.cos(j/3)
            cell_size = base_size * size_factor
            
            # Center position with some randomness
            x = i * (10/rows) + random.uniform(-0.1, 0.1)
            y = j * (10/cols) + random.uniform(-0.1, 0.1)
            
            # Randomly choose rotation with smoother transitions
            angle = (i * j) % 90 + random.uniform(-10, 10)
            
            # Alternate between shapes
            shape_type = random.choice(['square', 'diamond', 'circle'])
            color = random.choice(colors)
            
            if shape_type == 'square':
                rect = patches.Rectangle(
                    (x - cell_size/2, y - cell_size/2),
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
                    radius=cell_size/np.sqrt(2),
                    orientation=np.radians(angle),
                    facecolor=color,
                    alpha=0.7
                )
                ax.add_patch(diamond)
            else:  # circle
                circle = patches.Circle(
                    (x, y),
                    radius=cell_size/2,
                    facecolor=color,
                    alpha=0.7
                )
                ax.add_patch(circle)

    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='black')
    plt.close()

def generate_refined_rectangles(output_file):
    """
    Generates an abstract pattern with structured overlapping semi-transparent rectangles.
    """
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.axis('off')

    # Number of rectangles
    num_rectangles = 50

    for _ in range(num_rectangles):
        # Fixed-width and height ranges for rectangles
        width = random.uniform(10, 30)
        height = random.uniform(10, 30)
        
        # Random position
        x = random.uniform(-50, 50)
        y = random.uniform(-50, 50)

        # Random rotation angle, keeping it subtle
        angle = random.choice([0, 15, 30, -15, -30])

        # Random color with transparency
        color = (0, random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.3, 0.7))  # Teal shades

        rectangle = patches.Rectangle((x, y), width, height, angle=angle, color=color, alpha=color[3], ec="none")
        ax.add_patch(rectangle)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    parser = argparse.ArgumentParser(description='Generate various types of artistic patterns')
    parser.add_argument('style', choices=['noise', 'radial', 'squares', 'rectangles'],
                        help='The style of art to generate')
    parser.add_argument('-o', '--output', default='art.png',
                        help='Output file name (default: art.png)')

    args = parser.parse_args()

    # Map of style names to generator functions
    generators = {
        'noise': generate_noise,
        'radial': generate_radial,
        'squares': generate_squares,
        'rectangles': generate_refined_rectangles
    }

    # Generate the art
    print(f"Generating {args.style} art...")
    generators[args.style](args.output)
    print(f"Art saved to {args.output}")

if __name__ == '__main__':
    main()
