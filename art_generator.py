#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import argparse

def generate_noise(output_file):
    """
    Generates a complex abstract diagram of overlapping polygons and lines.
    """
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
    Generates a grid of black shapes, alternating between squares and diamonds, with random rotations.
    """
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

    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    parser = argparse.ArgumentParser(description='Generate various types of artistic patterns')
    parser.add_argument('style', choices=['noise', 'radial', 'squares'],
                      help='The style of art to generate')
    parser.add_argument('-o', '--output', default='art.png',
                      help='Output file name (default: art.png)')

    args = parser.parse_args()

    # Map of style names to generator functions
    generators = {
        'noise': generate_noise,
        'radial': generate_radial,
        'squares': generate_squares
    }

    # Generate the art
    print(f"Generating {args.style} art...")
    generators[args.style](args.output)
    print(f"Art saved to {args.output}")

if __name__ == '__main__':
    main()
