import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig, ax = plt.subplots()

# Generate snake body using parametric equations for curves
t = np.linspace(0, 4 * np.pi, 500)
x = t * np.cos(t) / 2
y = t * np.sin(t) / 2

# Draw the snake body with a gradient color effect (alternating green shades)
for i in range(len(t)-1):
    ax.plot(x[i:i+2], y[i:i+2], color=('#006400' if i % 2 == 0 else '#32CD32'), linewidth=10)

# Add snake scales
for i in range(100):
    scale_x = x[i*5]
    scale_y = y[i*5]
    scale_size = 0.06  # Vary scale sizes a bit for texture effect
    scale_color = '#228B22' if i % 2 == 0 else '#2E8B57'
    ellipse = plt.Circle((scale_x, scale_y), scale_size, color=scale_color, alpha=0.9)
    ax.add_patch(ellipse)

# Snake head as an ellipse
snake_head_x = x[-1] + 0.15
snake_head_y = y[-1]
head = plt.Circle((snake_head_x, snake_head_y), 0.2, color='green')
ax.add_patch(head)

# Add eyes to the snake head
eye_left = plt.Circle((snake_head_x - 0.06, snake_head_y + 0.1), 0.03, color='black')
eye_right = plt.Circle((snake_head_x + 0.06, snake_head_y + 0.1), 0.03, color='black')
ax.add_patch(eye_left)
ax.add_patch(eye_right)

# Add snake tongue (using a zigzag pattern for realism)
tongue_x = [snake_head_x + 0.1, snake_head_x + 0.15, snake_head_x + 0.1, snake_head_x + 0.2]
tongue_y = [snake_head_y - 0.05, snake_head_y - 0.12, snake_head_y - 0.18, snake_head_y - 0.25]
ax.plot(tongue_x, tongue_y, color='red', linewidth=2)

# Make the snake body curvier to look more "wild" and natural
for i in range(50):
    curve_x = x[i*10:i*10+10] + np.random.normal(0, 0.02, 10)
    curve_y = y[i*10:i*10+10] + np.random.normal(0, 0.02, 10)
    ax.plot(curve_x, curve_y, color='green', linewidth=8)

# Set the plot limits to frame the snake
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_aspect('equal')
ax.axis('off')

# Display the snake drawing
plt.show()
