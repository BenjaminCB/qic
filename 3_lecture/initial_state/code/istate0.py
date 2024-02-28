#

# Import tools
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Define initial_state as |0> ; apply initialisation to the 0th qubit ; draw circuit
initial_state = [1, 0]
qc.initialize(initial_state, 0)
qc.draw('mpl', filename="Lectures/#3/initial_state/results/initial_state_0")

# Define initial_state as |1> ; apply initialisation to the 0th qubit ; draw circuit
initial_state = [0, 1]
qc.initialize(initial_state, 0)
qc.draw('mpl', filename="Lectures/#3/initial_state/results/initial_state_0")

