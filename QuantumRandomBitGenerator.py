from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# user input
no_of_bits = int(input("Enter the number of bits: "))
 
# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the circuit on a simulator
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(qc, shots=no_of_bits)
result = job.result()

# Get the counts (the number of times each result occurred)
counts = result.get_counts()

# Print the generated random bits
print("Random bits generated:")
for bitstring, count in counts.items():
    print(f"{bitstring}: occurred {count} times")

# Optionally, plot the distribution of results
plt.bar(counts.keys(), counts.values())
plt.xlabel('Bitstring')
plt.ylabel('Count')
plt.title(f'Distribution of Random Bits over {no_of_bits} shots')
plt.show()