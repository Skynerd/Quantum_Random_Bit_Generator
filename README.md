# Quantum Random Bit Generator

## Overview
This project implements a Quantum Random Bit Generator using Qiskit. It leverages the principles of quantum mechanics to generate random bits through the use of quantum circuits. By applying the Hadamard gate to a qubit, the circuit creates superposition, and upon measurement, yields a distribution of random bits.

## Features
- Generates random bits based on user-defined input.
- Utilizes Qiskit's quantum circuit simulation capabilities.
- Visualizes the distribution of generated random bits using Matplotlib.

## Requirements
- Python 3.11
- Qiskit 1.2.2
- Matplotlib 3.8.1

## Installation
To set up the project, follow these steps:
1. **Clone the repository**: 
```bash
git clone https://github.com/yourusername/quantum-random-bit-generator.git cd quantum-random-bit-generator
```
2. **Install the required packages**:
```bash
pip install qiskit matplotlib
``` 
 
## Usage
1. Run the script:
```bash
python quantum_random_bit_generator.py
```
2. Input the number of bits you want to generate when prompted: 
```bash
Enter the number of bits: 10
``` 
3. The program will display the generated random bits and their occurrence counts, as well as a bar chart visualizing the distribution of the results.

## Code Structure
- **quantum_random_bit_generator.py**: The main script that generates random bits and visualizes the distribution.

## Example Output
When the script is run, you will see an output similar to:
```bash
Random bits generated: 
0: occurred 5 times 
1: occurred 5 times
```
And a bar chart displaying the distribution of the random bits generated.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
