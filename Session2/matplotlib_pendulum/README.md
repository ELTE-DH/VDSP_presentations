# matplotlib_pendulum

Develop a double-pendulum simulation using Python and Matplotlib, designed for visualization and educational purposes. The simulation includes animations and two sliders to adjust the link sizes on the fly.

## Overview

The project comprises a double-pendulum simulation implemented in Python using Matplotlib for animations and user interface components. The architecture features:

- **Backend**: Handles the double-pendulum dynamics, randomizes initial conditions, and captures angular positions over time.
- **Frontend**: Displays the animation, includes sliders for adjusting link sizes, and manages user interactions.

### Project Structure

- `main.py`: Initializes the simulation, sets up the animation, and manages the user interface.
- `pendulum.py`: Implements the double-pendulum dynamics and numerical integration using the Runge-Kutta method.
- `utils.py`: Contains utility functions for data visualization, such as showing y positions over time.

## Features

- **Visualization**: Animates the double-pendulum system using Matplotlib.
- **Educational Tool**: Demonstrates the chaotic behavior of a double-pendulum.
- **User Interface**: Two sliders to adjust the lengths of the pendulum links in real-time.
- **Data Output**: Outputs the angular positions of both nodes as a function of time upon window closure.
- **Y Position Visualization**: A button to display the y positions of the two nodes over time in a popup window.

## Getting started

### Requirements

- Python 3.6+
- Matplotlib
- NumPy

### Quickstart

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd matplotlib_pendulum
   ```
2. Install the required packages:
   ```sh
   pip install matplotlib numpy
   ```
3. Run the simulation:
   ```sh
   python main.py
   ```

## License

Copyright (c) 2024.
