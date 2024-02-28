#
# https://qiskit.github.io/qiskit-aer/tutorials/1_aer_provider.html#Simulating-a-quantum-circuit

# Import tools
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi

qc = QuantumCircuit(1) # Create a quantum circuit with one qubit

initial_state = [0,1]   # Define initial_state as |1>  ; = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>
qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
# Let's view our circuit
qc.draw('mpl', filename="Lectures/#3/measurement/results/istate")



# -------------------------------------------------------------------------------------------------------------
shots = 5
sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit

qc.save_statevector()   # Tell simulator to save statevector
qobj = assemble(qc, shots=shots)     # Create a Qobj from the circuit for the simulator to run
result = sim.run(qobj).result() # Do the simulation and return the result


out_state = result.get_statevector()
print(out_state) # Display the output state vector

qc.measure_all()
qc.draw()

qobj = assemble(qc)
result = sim.run(qobj).result()
counts = result.get_counts()
plot_histogram(counts)






  
