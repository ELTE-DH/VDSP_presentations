import matplotlib.pyplot as plt

def show_y_positions(time_points, y1_positions, y2_positions):
    try:
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(time_points, y1_positions, label='Y1 Position')
        ax2.plot(time_points, y2_positions, label='Y2 Position')
        
        ax1.set_title('Y1 Position Over Time')
        ax2.set_title('Y2 Position Over Time')
        
        ax1.set_ylabel('Y1 Position')
        ax2.set_ylabel('Y2 Position')
        ax2.set_xlabel('Time')

        ax1.legend()
        ax2.legend()

        plt.show()
    except Exception as e:
        print(f"An error occurred while showing y positions: {e}")
        import traceback
        traceback.print_exc()