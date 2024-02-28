# Import relevant packages, functions, ...
from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi, log2
import os

# Define a function to map from statevector to dictionary
def statevector_to_dict(sv):
    bit_mask = f"0{int(log2(len(sv)))}b"
    return {format(i, bit_mask): v.real for i, v in enumerate(sv)} 

# Define quantum circuit and some initial statevectors
Q_circuit = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state0 = [0, 1]   # Define initial_state as |1>
initial_state1 = [1, 0]   # Define initial_state as |0>
initial_state2 = [1/sqrt(2), 1/sqrt(2)]

# Apply initialisation operation to the 0th qubit
Q_circuit.initialize(initial_state2, 0)
Q_circuit.draw('mpl', filename="Lectures/#3/measurement/results/init_state")


# Run the quantum circuit on a statevector simulator backend
simulator = Aer.get_backend('statevector_simulator')

# Create a Quantum program for execution
job = simulator.run(Q_circuit)
result = job.result()
outputstate = result.get_statevector(Q_circuit, decimals=3)
print(outputstate)

# Map statevector to dictionary
sv_dict = statevector_to_dict(outputstate.data)
plot_histogram(sv_dict, legend=None, color=['crimson'], title="Histogram", filename="Lectures/#3/measurement/results/hist")
