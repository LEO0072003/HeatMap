import matplotlib.tri as tri
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial


# Create the initial heatmap figure
fig, ax = plt.subplots()

vmin = 0
vmax = 4000
heatmap = ax.imshow(np.zeros((4, 4)), cmap='coolwarm', vmin=vmin, vmax=vmax)
# heatmap.set_clim(vmin=vmin, vmax=4000)

ax.set_title("Heatmap")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")


cbar = fig.colorbar(heatmap, ax=ax)


# def rand():
#     s = '1500'
#     for i in range(16):
#         a = random.randint(0,4000)
#         s+=f',{a}'

#     return s


# Define the update function for the heatmap data
def update_heatmap(data):
    # Extract the distance and values from the data list
    distance = data[0]
    values = data[1:]

    # Reshape the values into a 4x4 array
    values_arr = np.array(values).reshape((4, 4))
    im = ax.imshow(values_arr, cmap='coolwarm', vmin=vmin, vmax=vmax)


    # Update the heatmap data and annotations
    heatmap.set_data(values_arr)

    # Set the heatmap title and distance annotation
    ax.set_title(f"Heatmap (distance={distance})")

    return heatmap,

# Define the animation function to update the heatmap every 100ms (10 times per second)
def animate(i):
    # Read one line of input from the serial port

    input_str = ser.readline().decode().strip()
    # input_str = rand()

    # Convert the input string to a list of integers
    input_list = [int(x) for x in input_str.split(',')]


    #adjusting the values between 0 and 4000
    for i in range(1,len(input_list)):
        if(input_list[i]>4000):
            input_list[i] = 4000
        elif(input_list[i]<0):
            input_list[i] = 0


    # Pass the input list to the update function
    return update_heatmap(input_list)

# Initialize the serial connection
ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the port name on your system

# Start the animation
ani = animation.FuncAnimation(fig, animate, interval=100)


# Show the heatmap
plt.show()
