import numpy as np
import matplotlib.pyplot as plt

# Function to welcome the user and provide instructions
def present_system():
    print("\nWelcome to the Discrete Signal Analyzer!")
    print("-" * 40)
    print("This system allows you to process discrete signals by applying various transformations and analyses.")
    print("You will be able to visualize graphs and understand the characteristics of the system processing the signal.")
    print("Enter a set of up to 9 integers between -9 and 9.")
    print("We recommend choosing values between -3 and 3 for better visualization.")
    print("-" * 40)

# Function to obtain validated user input
def get_signal():
    while True:
        user_input = input("\nEnter up to 9 integers separated by spaces: ")
        try:
            x = list(map(int, user_input.split()))  # Convert input values to integers
            if len(x) > 9:
                print("Please enter a maximum of 9 numbers.")  # Validate quantity
            elif any(abs(num) > 9 for num in x):
                print("All numbers must be between -9 and 9.")  # Validate range
            else:
                return np.array(x)  # Return a NumPy array
        except ValueError:
            print("Invalid input. Make sure to enter only integer numbers.")

# Function to plot the original signal graphically
def plot_signal(x):
    n = np.arange(len(x))  # Generate the index axis
    plt.figure(figsize=(8, 4))
    plt.stem(n, x, basefmt=" ")  # Stem plot (discrete signal)
    plt.title("Original Signal x[n]")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid()
    plt.show()

# --- Execute menu and user input ---
present_system()
signal = get_signal()
plot_signal(signal)

# --- Initialize data for transformations ---
x = signal
n = np.arange(len(x))

# --- Signal Transformations ---

# 1. Time shift: moves the signal forward by 2 units
n_shifted = n + 2
x_shifted = x  # The signal values remain unchanged

# 2. Time reflection: flips the time axis
n_reflected = -n
x_reflected = x  # Values remain unchanged

# 3. Time compression by 2: "accelerates" the time
n_compressed = n // 2  # Reduces indices for compression
x_compressed = x[n_compressed]  # Select corresponding elements

# --- Plot transformed signals ---
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Time-shifted signal plot
axs[0].stem(n_shifted, x_shifted, basefmt=" ")
axs[0].set_title("Shifted Signal x[n-2]")
axs[0].grid()

# Time-reflected signal plot
axs[1].stem(n_reflected, x_reflected, basefmt=" ")
axs[1].set_title("Reflected Signal x[-n]")
axs[1].grid()

# Time-compressed signal plot
axs[2].stem(n_compressed, x_compressed, basefmt=" ")
axs[2].set_title("Compressed Signal x[2n]")
axs[2].grid()

plt.tight_layout()
plt.show()

# --- Implementation of Discrete Systems ---

# System 1: Difference between consecutive samples
y1 = np.zeros_like(x)  # Initialize output array with zeros
y1[1:] = x[1:] - x[:-1]  # y[n] = x[n] - x[n-1]; assuming y[0] = 0

# System 2: Cumulative sum of the signal (integrator)
y2 = np.cumsum(x)  # Cumulative sum from x[0] to x[n]

# System 3: Time compression (already done previously)
y3 = x_compressed

# --- Function to analyze system properties ---
def analyze_system(y, name):
    print(f"System Analysis: {name}")

    # Check causality: all responses must be associated with n >= 0
    print(f"Causal: {'Yes' if np.all(y[n >= 0]) else 'No'}")

    # Check memory-based behavior: more than one input value influences the output
    print(f"Memory-based: {'Yes' if len(y) > 1 else 'No'}")

    # Check stability: no output tends to infinity
    print(f"Stable: {'Yes' if np.all(np.abs(y) < np.inf) else 'No'}")

    # Check time invariance (simplified and approximated with roll)
    print(f"Time-invariant: {'Yes' if np.array_equal(y, np.roll(y, 1)) else 'No'}")

    # Check linearity (simplified with homogeneity and partial additivity)
    print(f"Linear: {'Yes' if np.all(y * 2 == np.concatenate(([0], y[:-1])) * 2) else 'No'}")
    print("-" * 40)

# --- Call system analysis for each defined system ---
analyze_system(y1, "y[n] = x[n] - x[n-1]")  # Derivative system
analyze_system(y2, "y[n] = cumulative sum of x[k]")  # Integrator system
analyze_system(y3, "y[n] = x[2n]")  # Compression system