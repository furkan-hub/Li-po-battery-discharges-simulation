import time
import matplotlib.pyplot as plt

# Battery specifications
initial_capacity = 2000  # Initial capacity (mAh)
initial_voltage = 4.2  # Initial voltage (V)
discharge_voltage = 3.0  # Discharge voltage (V)
discharge_rate = 100  # Discharge rate (mAh)

# Time and voltage lists
time = []
voltage = []

current_capacity = initial_capacity
current_voltage = initial_voltage
time_counter = 0

while current_voltage > discharge_voltage:
    time.append(time_counter)
    voltage.append(current_voltage)
    current_capacity -= discharge_rate
    current_voltage = (current_capacity / initial_capacity) * initial_voltage
    time_counter += 1

# Plotting the graph
plt.plot(time, voltage)
plt.xlabel("Time (Minutes)")
plt.ylabel("Voltage (V)")
plt.title("Li-po Battery Discharge Simulation")
plt.grid(True)
plt.show()
