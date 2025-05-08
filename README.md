# 📡 Discrete Signal Analyzer - EN US

## Overview
The **Discrete Signal Analyzer** is a Python-based tool for processing discrete-time signals by applying **transformations** (time shift, reflection, and compression) and **analyzing system properties** (causality, memory, stability, time invariance, and linearity). It allows users to input a **custom signal** and observe the transformed outputs through graphical representations.

## 🔧 Features
- Accepts **up to 9 integers** as input for signal processing.
- Applies the following **signal transformations**:
  - **Time Shift**: Moves the signal forward by 2 units.
  - **Time Reflection**: Flips the signal over the time axis.
  - **Time Compression**: Reduces the time scale by a factor of 2.
- Implements **three discrete systems** for analysis:
  - **System 1**: Difference between consecutive samples \( y[n] = x[n] - x[n-1] \).
  - **System 2**: Cumulative sum (integrator) \( y[n] = \sum x[k] \).
  - **System 3**: Time compression \( y[n] = x[2n] \).
- Evaluates **five properties** of each system:
  - **Causality**
  - **Memory**
  - **Stability**
  - **Time Invariance**
  - **Linearity**
- Generates **stem plots** for visualizing discrete-time signals.

---

## 🚀 How to Install & Run

### Prerequisites
Ensure you have Python installed (version **3.6+** recommended). Also, install the necessary dependencies:
```bash
pip install numpy matplotlib
```

### Running the Script
Clone the repository or download the script:
```bash
git clone https://github.com/your-username/discrete-signal-analyzer.git
cd discrete-signal-analyzer
```
Run the Python script:
```bash
python signal_analyzer.py
```

Upon execution:
1. The program will **ask for a sequence of up to 9 numbers**.
2. The script will validate the input and process the signal.
3. **Graphs** will be generated to visualize the **original signal** and **transformed signals**.
4. The system analysis will be displayed in the **terminal**.

---

## 🖥️ Example Usage
### Input:
```
Enter up to 9 integers separated by spaces: 0 -2 -1 0 1 2 3 0 0
```

### Output:
**Graphical Representation**
✅ Original Signal  
✅ Shifted Signal \( x[n-2] \)  
✅ Reflected Signal \( x[-n] \)  
✅ Compressed Signal \( x[2n] \)  

**Terminal Analysis**
```
System Analysis: y[n] = x[n] - x[n-1]
  Causal: Yes
  Memory-based: Yes
  Stable: Yes
  Time-invariant: No
  Linear: Yes
----------------------------------------
System Analysis: y[n] = cumulative sum of x[k]
  Causal: Yes
  Memory-based: Yes
  Stable: Yes
  Time-invariant: No
  Linear: Yes
----------------------------------------
System Analysis: y[n] = x[2n]
  Causal: Yes
  Memory-based: No
  Stable: Yes
  Time-invariant: Yes
  Linear: Yes
----------------------------------------
```

---

## 📌 Notes & Limitations
- The input signal **must be integers** in the range **-9 to 9**.
- The system **assumes causal behavior** based on non-negative indices.
- The **cumulative sum system is limited** to the input size provided.
- The **compressed signal may discard some values** depending on the length.

---

## 🤝 Contributing
Have ideas for improving the project? Feel free to **fork** this repository and submit **pull requests**! If you encounter issues, please report them in the **GitHub Issues** section.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---