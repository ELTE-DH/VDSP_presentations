import matplotlib.pyplot as plt
import numpy as np
from pendulum import DoublePendulum
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
from utils import show_y_positions

def main():
    try:
        # Initialize DoublePendulum with random initial conditions and damping
        pendulum = DoublePendulum(
            theta1=np.random.uniform(0, 2*np.pi),
            theta2=np.random.uniform(0, 2*np.pi),
            omega1=np.random.uniform(0, 2*np.pi),
            omega2=np.random.uniform(0, 2*np.pi),
            damping=5.5e-3  # Adding damping coefficient
        )

        # Set up the figure, the axis, and the plot elements
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.35)  # Adjust the main plot to make room for sliders and button
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal')

        # Line objects for the pendulum arms
        line, = ax.plot([], [], lw=2)
        # Dot objects for the pendulum bobs
        dot1, = ax.plot([], [], 'bo')
        dot2, = ax.plot([], [], 'ro')

        # Initialize lists to store y positions and time points
        y1_positions = []
        y2_positions = []
        time_points = []
        start_time = 0

        # Function to initialize the plot
        def init():
            line.set_data([], [])
            dot1.set_data([], [])
            dot2.set_data([], [])
            return line, dot1, dot2

        # Function to update the plot
        def update(frame):
            nonlocal start_time
            state = pendulum.step(1/30)  # Update pendulum state (30 FPS)
            x1 = pendulum.l1 * np.sin(pendulum.theta1)
            y1 = -pendulum.l1 * np.cos(pendulum.theta1)
            x2 = x1 + pendulum.l2 * np.sin(pendulum.theta2)
            y2 = y1 - pendulum.l2 * np.cos(pendulum.theta2)

            # Collect y positions and time points
            y1_positions.append(y1)
            y2_positions.append(y2)
            time_points.append(start_time)
            start_time += 1/30

            line.set_data([0, x1, x2], [0, y1, y2])
            dot1.set_data([x1], [y1])
            dot2.set_data([x2], [y2])
            return line, dot1, dot2

        # Create the animation
        ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 300), init_func=init, blit=True, interval=1000/30)

        # Define slider axes
        axcolor = 'lightgoldenrodyellow'
        ax_l1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
        ax_l2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

        # Create sliders
        s_l1 = Slider(ax_l1, 'Link 1 Length', 0.1, 2.0, valinit=pendulum.l1)
        s_l2 = Slider(ax_l2, 'Link 2 Length', 0.1, 2.0, valinit=pendulum.l2)

        # Slider update function
        def update_length(val):
            pendulum.l1 = s_l1.val
            pendulum.l2 = s_l2.val

        # Attach the update function to sliders
        s_l1.on_changed(update_length)
        s_l2.on_changed(update_length)

        # Define button axes and create button
        ax_button = plt.axes([0.35, 0.025, 0.3, 0.05])  # Make the button larger
        btn_show_y_positions = Button(ax_button, 'Show Y Positions')

        # Attach the show_y_positions function to the button
        def on_show_y_positions(event):
            show_y_positions(time_points, y1_positions, y2_positions)

        btn_show_y_positions.on_clicked(on_show_y_positions)

        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()