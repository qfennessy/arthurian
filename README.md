# Arthurian

A Python-based art generation tool that creates unique abstract compositions using various geometric patterns and styles.

## Description

Arthurian is a versatile art generation tool that creates abstract compositions using different geometric patterns and styles. Each style produces unique visual outputs with distinct characteristics, making it suitable for generating art for various purposes.

## Features

- Multiple art generation styles:
  - `noise`: Complex abstract diagrams with overlapping polygons and lines
  - `radial`: Colorful radial patterns with lines radiating outward
  - `squares`: Grid-based patterns with alternating squares and diamonds
  - `rectangles`: Structured compositions with semi-transparent teal rectangles

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Generate art using the command line interface:

```bash
python art_generator.py STYLE -o output.png
```

Where `STYLE` can be one of: `noise`, `radial`, `squares`, or `rectangles`

Examples:
```bash
python art_generator.py noise -o abstract_noise.png
python art_generator.py radial -o radial_pattern.png
python art_generator.py squares -o geometric_squares.png
python art_generator.py rectangles -o teal_rectangles.png
```

## Requirements

- Python 3.7+
- matplotlib
- numpy
- Additional dependencies listed in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
