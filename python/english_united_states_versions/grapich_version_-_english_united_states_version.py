# Importing necessary libraries
import numpy as np                          # For numerical and array operations
import matplotlib.pyplot as plt             # For graph plotting
import tkinter as tk                        # For creating the graphical interface
from tkinter import messagebox              # For displaying popup messages
from tkinter import ttk                     # For using modern widgets (such as tabs)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # For embedding Matplotlib graphs in Tkinter

def get_system_analysis(x):
    """Generates a string with the analysis of systems based on the input signal x."""
    n = np.arange(len(x))  # Index array
    result_str = ""        # Initialize result string

    # --- System 1: Difference between consecutive samples ---
    y1 = np.zeros_like(x)               # Initialize output array
    y1[1:] = x[1:] - x[:-1]             # y[n] = x[n] - x[n-1], with y[0] = 0
    result_str += "System 1: y[n] = x[n] - x[n-1]\n"
    result_str += "  Causal: Yes\n  Memory-based: Yes\n  Stable: Yes\n  Time-invariant: No\n  Linear: Yes\n"
    result_str += "-" * 40 + "\n\n"

    # --- System 2: Cumulative Sum ---
    y2 = np.cumsum(x)                   # y[n] = cumulative sum up to n
    result_str += "System 2: y[n] = cumulative sum of x[k]\n"
    result_str += "  Causal: Yes\n  Memory-based: Yes\n  Stable: Yes\n  Time-invariant: No\n  Linear: Yes\n"
    result_str += "-" * 40 + "\n\n"

    # --- System 3: Time Compression ---
    n_compressed = n // 2               # Index values for time compression
    y3 = x[n_compressed] if len(n_compressed) <= len(x) else x  # y[n] = x[2n]
    result_str += "System 3: y[n] = x[2n]\n"
    result_str += "  Causal: Yes\n  Memory-based: No\n  Stable: Yes\n  Time-invariant: Yes\n  Linear: Yes\n"
    result_str += "-" * 40 + "\n"

    return result_str

def update_signals_tab(x):
    """Updates the 'Signals' tab by displaying the original signal and its transformations."""
    n = np.arange(len(x))  # Signal indices

    # --- Original Signal Graph ---
    fig_orig = plt.Figure(figsize=(6, 3), dpi=100)
    ax_orig = fig_orig.add_subplot(111)
    ax_orig.stem(n, x, basefmt=" ")       # Stem plot
    ax_orig.set_title("Original Signal x[n]")
    ax_orig.grid(True)

    # --- Transformed Signal Graphs ---
    fig_trans = plt.Figure(figsize=(6, 8), dpi=100)

    # Time Shift: x[n-2]
    ax1 = fig_trans.add_subplot(311)
    ax1.stem(n + 2, x, basefmt=" ")
    ax1.set_title("Shifted Signal x[n-2]")
    ax1.grid(True)

    # Time Reflection: x[-n]
    ax2 = fig_trans.add_subplot(312)
    ax2.stem(-n, x, basefmt=" ")
    ax2.set_title("Reflected Signal x[-n]")
    ax2.grid(True)

    # Time Compression: x[2n]
    ax3 = fig_trans.add_subplot(313)
    n_compressed = n // 2
    x_compressed = x[n_compressed] if len(n_compressed) <= len(x) else x
    ax3.stem(n_compressed, x_compressed, basefmt=" ")
    ax3.set_title("Compressed Signal x[2n]")
    ax3.grid(True)

    # Removing previous widgets from the tab
    for widget in frameSignals.winfo_children():
        widget.destroy()

    # --- Creating a scrollable container ---
    canvasFrame = tk.Frame(frameSignals)
    canvasFrame.pack(fill=tk.BOTH, expand=True)

    scroll_signals = tk.Scrollbar(canvasFrame)
    scroll_signals.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(canvasFrame, yscrollcommand=scroll_signals.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scroll_signals.config(command=canvas.yview)

    # Internal frame to place the graphs
    frame_inner = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_inner, anchor="nw")

    # Adding the original signal graph
    canvas_orig = FigureCanvasTkAgg(fig_orig, master=frame_inner)
    canvas_orig.draw()
    canvas_orig.get_tk_widget().pack(pady=5)

    # Adding the transformed signal graphs
    canvas_trans = FigureCanvasTkAgg(fig_trans, master=frame_inner)
    canvas_trans.draw()
    canvas_trans.get_tk_widget().pack(pady=5)

    # Updating the scrollable area
    frame_inner.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def process_signal():
    """Validates user input, processes the signal, and updates the interface."""
    input_data = entry.get()
    try:
        # Convert input to a list of integers
        x_list = list(map(int, input_data.split()))

        # Validate number of elements
        if len(x_list) > 9:
            messagebox.showerror("Error", "Enter a maximum of 9 numbers.")
            return
        # Validate value range
        elif any(abs(num) > 9 for num in x_list):
            messagebox.showerror("Error", "Numbers must be between -9 and 9.")
            return
        x = np.array(x_list)  # Convert to numpy array
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Enter only integers.")
        return

    # Update graphs
    update_signals_tab(x)

    # Update system analysis text
    analysis_str = get_system_analysis(x)
    textAnalysis.config(state="normal")
    textAnalysis.delete("1.0", tk.END)
    textAnalysis.insert(tk.END, analysis_str)
    textAnalysis.config(state="disabled")

    # Switch to the "Signals" tab automatically
    notebook.select(tab_signals)

# --- Building the Graphical Interface ---

# Creating the main window
root = tk.Tk()
root.title("Discrete Signal Analyzer")
root.geometry("800x800")

# Top frame with instructions and input
frameInput = tk.Frame(root)
frameInput.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

tk.Label(frameInput, text="Welcome to the Discrete Signal Analyzer!", font=("Arial", 16)).pack()
tk.Label(frameInput, text="Enter up to 9 integers between -9 and 9, separated by spaces.", font=("Arial", 12)).pack()
tk.Label(frameInput, text="We recommend choosing values between -3 and 3.", font=("Arial", 12)).pack(pady=5)

# Input field
entry = tk.Entry(frameInput, font=("Arial", 12), width=40)
entry.pack(pady=5)

# Button to process the signal
btnProcess = tk.Button(frameInput, text="Process Signal", font=("Arial", 12), command=process_signal)
btnProcess.pack(pady=5)

# Notebook with tabs: Signals and Analysis
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# "Signals" Tab
tab_signals = tk.Frame(notebook)
notebook.add(tab_signals, text="Signals")
frameSignals = tk.Frame(tab_signals)
frameSignals.pack(fill=tk.BOTH, expand=True)

# "System Analysis" Tab
tab_analysis = tk.Frame(notebook)
notebook.add(tab_analysis, text="System Analysis")

frame_analysis = tk.Frame(tab_analysis)
frame_analysis.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

scrollbar_analysis = tk.Scrollbar(frame_analysis)
scrollbar_analysis.pack(side=tk.RIGHT, fill=tk.Y)

# Text box for system analysis
textAnalysis = tk.Text(frame_analysis, wrap=tk.WORD, font=("Arial", 12), yscrollcommand=scrollbar_analysis.set)
textAnalysis.pack(fill=tk.BOTH, expand=True)
scrollbar_analysis.config(command=textAnalysis.yview)
textAnalysis.config(state="disabled")  # Initially disabled

# Start the interface main loop
root.mainloop()