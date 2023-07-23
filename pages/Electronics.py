import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants for PT100 sensor (Callendar-Van Dusen coefficients)
R0 = 100.0  # Resistance at 0 degrees Celsius (in ohms)
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

def pt100_resistance(temperature):
    # Calculate resistance from temperature using the Callendar-Van Dusen equation (inverse form)
    R = R0 * (1 + A * temperature + B * temperature**2 + C * (temperature - 100) * temperature**3)
    return R
st.title("Electronics")
with st.expander("Analog Battery Level Indicator"):
    st.image("images/circuit (3).png")
    st.markdown("""
    ### Requirements:
    - **Voltage Range:** 20 V to 21.2 V        <span style="color:red">&#x25CF;</span>
    - **Voltage Range:** 21.3 V to 23.5 V        <span style="color:yellow">&#x25CF;</span>
    - **Voltage Range:** 23.6 V to 24.9 V        <span style="color:green">&#x25CF;</span>
    - **Voltage Range:** 25+ V        <span style="color:blue">&#x25CF;</span>
    """, unsafe_allow_html=True)
    st.markdown("[Analog Battery Level Indicator EveryCircuit](https://everycircuit.com/circuit/6404912369631232/voltagemeter)")
with st.expander("Wheatstone Bridge Circuit for PT100 temp readings"):
    st.title("PT100 Resistance Calculator")

    # Input temperature with a slider
    temperature = st.slider("Select Temperature (°C):", min_value=-200.0, max_value=850.0, value=0.0, step=0.1)

    # Calculate resistance
    resistance = pt100_resistance(temperature)

    # Display the resistance
    st.write(f"Resistance: {resistance:.2f} ohms")

    # Create a plot to visualize the resistance-temperature relationship
    temperature_values = np.linspace(-200, 850, 100)
    resistance_values = [pt100_resistance(T) for T in temperature_values]

    # Use Matplotlib to create the plot
    plt.figure()
    plt.plot(temperature_values, resistance_values, label='Resistance (ohms)')
    plt.title('Resistance vs Temperature (PT100)')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Resistance (ohms)')
    plt.legend()
    plt.grid(True)

    # Show the plot using Streamlit
    st.pyplot(plt)
    st.markdown("[Wheatstone Bridge](https://everycircuit.com/circuit/6156812778471424/pt100-with-wheatstone-bridge-and-op-amp)")
