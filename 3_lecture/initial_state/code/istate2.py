#

# Import tools
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Define initial_state as i/sqrt(2)*|0> + 1/sqrt(2)*|1> ; apply initialisation to the 0th qubit ; draw circuit
initial_state2 = [1j/sqrt(2), 1/sqrt(2)]
qc.initialize(initial_state2, 0)
qc.draw('mpl', filename="Lectures/#3/initial_state/results/state2")
