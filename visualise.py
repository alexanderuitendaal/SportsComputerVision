import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
from PIL import Image
from matplotlib.animation import FuncAnimation

def draw_field_hockey_field(save_img = False):
    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Set the aspect ratio of the plot
    ax.set_aspect('equal')

    # Set the limits of the plot
    ax.set_xlim(-10, 110)
    ax.set_ylim(-10, 70)

    # Draw the margin outside the grass pitch
    margin = Rectangle((-10, -10), 120, 80, linewidth=2, edgecolor='white', facecolor='darkgreen')
    ax.add_patch(margin)

    # Draw the grass pitch
    pitch = Rectangle((0, 0), 100, 60, linewidth=2, edgecolor='white', facecolor='darkgreen')
    ax.add_patch(pitch)

    # Draw the vertical lines dividing the field
    line1 = plt.Line2D([25, 25], [0, 60], linewidth=2, color='white')
    line2 = plt.Line2D([50, 50], [0, 60], linewidth=2, color='white')
    line3 = plt.Line2D([75, 75], [0, 60], linewidth=2, color='white')
    ax.add_artist(line1)
    ax.add_artist(line2)
    ax.add_artist(line3)

    # Draw the goal areas
    # goal1 = Rectangle((0, 28), 2.34, 4.0, linewidth=2, edgecolor='white', facecolor='none')

    # this is the first goal 
    goalline1 = plt.Line2D([-2.34, 0.0], [28, 28], linewidth=2, color='white')    
    goalline2 = plt.Line2D([-2.34, 0.0], [32, 32], linewidth=2, color='white')    
    goalline3 = plt.Line2D([-2.34, -2.34], [28, 32], linewidth=2, color='white')    

    ax.add_artist(goalline1)
    ax.add_artist(goalline2)
    ax.add_artist(goalline3)

    goalline1_mirror = plt.Line2D([100, 102.34], [28, 28], linewidth=2, color='white')
    goalline2_mirror = plt.Line2D([100, 102.34], [32, 32], linewidth=2, color='white')
    goalline3_mirror = plt.Line2D([102.34, 102.34], [28, 32], linewidth=2, color='white')

    # Add the mirrored goal lines to the plot
    ax.add_artist(goalline1_mirror)
    ax.add_artist(goalline2_mirror)
    ax.add_artist(goalline3_mirror)
    
    # Draw the half circles encapsulating the goals
    goal_circle1 = Arc((0, 30), 29.26, 29.26, theta1=-90, theta2=90, linewidth=2, edgecolor='white', facecolor='none')
    goal_circle2 = Arc((100, 30), 29.26, 29.26, theta1=90, theta2=-90, linewidth=2, edgecolor='white', facecolor='none')
    ax.add_patch(goal_circle1)
    ax.add_patch(goal_circle2)

    # Set the tick labels and remove ticks
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(axis='both', which='both', length=0)

    # Set the title
    ax.set_title('Field Hockey Field')

    # Remove excess whitespace
    plt.subplots_adjust(0, 0, 1, 1)

    # Save the figure as a high-resolution image
    if save_img:
        plt.savefig('field_hockey_field.png', dpi=300)

    # Close the figure
    return fig, ax



# Function to update the plot
def update(frame):
    # Clear the previous player markers
    for marker in player_markers:
        marker.remove()
    player_markers.clear()

    # Update the players' positions (example update)
    player_positions[0] = (player_positions[0][0] + 1, player_positions[0][1])
    player_positions[1] = (player_positions[1][0] - 1, player_positions[1][1])
    player_positions[2] = (player_positions[2][0], player_positions[2][1] + 1)
    player_positions[3] = (player_positions[3][0], player_positions[3][1] - 1)

    # Draw the updated player markers
    for position in player_positions:
        marker = plt.Circle(position, 0.5, color='red', zorder=10)
        ax.add_patch(marker)
        player_markers.append(marker)


# Call the function to draw the field hockey field
fig, ax = draw_field_hockey_field()
# Initialize the players' positions (example data)
player_positions = [(20, 20), (40, 30), (60, 40), (80, 50)]
# Initialize an empty list to store the player markers
player_markers = []
# Create the animation
animation = FuncAnimation(fig, update, frames=500, interval=100)
# Display the animated plot
plt.show()



