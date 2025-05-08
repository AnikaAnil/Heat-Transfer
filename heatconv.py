import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Determination of Thermal Conductivity of Sawdust Using Lagged Pipe Apparatus")

# Expander for AIM
with st.expander("AIM"):
    st.write("""
    To determine the thermal conductivity of sawdust by knowing the thermal conductivity of Asbestos/MgO using lagged pipe apparatus.
    """)

# Expander for APPARATUS
with st.expander("APPARATUS REQUIRED"):
    st.write("""
    - Heater
    - Asbestos/MgO
    - Sawdust
    - Power supply
    """)

# Expander for THEORY
with st.expander("THEORY"):
    st.write("""
    Thermal insulation is a material which retards heat flow with reasonable effectiveness. Heat is transferred through insulation by conduction, convection, and radiation, or by the combination of these three. There is no insulation which is 100% effective to prevent the flow of heat under a temperature gradient.
    """)

# Expander for PROCEDURE
with st.expander("PROCEDURE"):
    st.write("""
    1. Switch ON the power supply.
    2. Switch ON the heater and set the dimmer to the required position.
    3. Wait for the steady-state condition.
    4. Note down the temperature, ammeter, and voltmeter readings.
    5. Substitute the recorded readings in the required formula.
    """)

# User Input for Readings
st.sidebar.header("Input Parameters")
voltage = st.sidebar.number_input("Voltage (V)", min_value=0.1, max_value=220.0, value=110.0)
current = st.sidebar.number_input("Current (A)", min_value=0.1, max_value=10.0, value=1.0)
temperature_surface = st.sidebar.number_input("Temperature at Surface (°C)", min_value=20, max_value=100, value=50)
temperature_ambient = st.sidebar.number_input("Ambient Temperature (°C)", min_value=20, max_value=100, value=25)
length = st.sidebar.number_input("Length of Pipe (m)", min_value=0.1, max_value=2.0, value=1.0)
radius = st.sidebar.number_input("Radius of Pipe (m)", min_value=0.01, max_value=1.0, value=0.05)

# Thermal conductivity formula
# Q = (V * I), where V is voltage, I is current
# Using Fourier's law for conduction to calculate thermal conductivity: 
# k = (Q * L) / (A * ΔT)
# Where:
# k = Thermal conductivity
# Q = Heat transfer rate (W)
# L = Length of the pipe (m)
# A = Cross-sectional area of the pipe (m²)
# ΔT = Temperature difference (°C)

# Calculate Q (Heat Transfer)
Q = voltage * current  # Heat transfer rate (W)

# Area of the cross-section of the pipe
A = np.pi * radius**2

# Temperature difference
delta_T = temperature_surface - temperature_ambient

# Thermal conductivity (k)
thermal_conductivity = (Q * length) / (A * delta_T)

# Output Results
st.subheader("Results")
st.write(f"Heat Transfer Rate (Q): {Q:.2f} W")
st.write(f"Temperature Difference (ΔT): {delta_T:.2f} °C")
st.write(f"Thermal Conductivity (k): {thermal_conductivity:.4f} W/m·K")

# Graphical representation (temperature vs heat transfer)
st.subheader("Graph: Temperature vs Heat Transfer Rate")

# Generate the graph to visualize the experiment
temperatures = np.linspace(20, 100, 10)
heat_transfer = voltage * current * np.ones_like(temperatures)  # Assuming constant power for simplicity

fig, ax = plt.subplots()
ax.plot(temperatures, heat_transfer, marker='o', color='blue', label="Heat Transfer")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Heat Transfer Rate (W)")
ax.set_title("Temperature vs Heat Transfer Rate")
ax.grid(True)
ax.legend()
st.pyplot(fig)
