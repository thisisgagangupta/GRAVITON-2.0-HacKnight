from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def create_oracle(num_frames):
    oracle_circuit = QuantumCircuit(num_frames)
    
    oracle_circuit.z(0) 
    
    return oracle_circuit
def apply_grover(circuit, oracle, num_iterations):
    grover_circuit = circuit.compose(oracle)
    for _ in range(num_iterations):
        grover_circuit.h(range(num_frames))
        grover_circuit.append(oracle, range(num_frames))
        grover_circuit.h(range(num_frames))
    
    return grover_circuit

def measure(circuit, num_frames):
    circuit.measure_all()
    return circuit
def simulate(circuit, backend='qasm_simulator', shots=1024):
    backend = Aer.get_backend(backend)
    job = execute(circuit, backend, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts

def remove_duplicates(num_frames, num_iterations):
    qc = QuantumCircuit(num_frames, num_frames)
    
    oracle = create_oracle(num_frames)
    grover_circuit = apply_grover(qc, oracle, num_iterations)
    
    grover_circuit = measure(grover_circuit, num_frames)
    
    counts = simulate(grover_circuit)
    
    measurement_outcome = max(counts, key=counts.get)
    duplicate_index = int(measurement_outcome, 2)
    
    return duplicate_index

# Example usage
num_frames = 8 
num_iterations = 2 

duplicate_index = remove_duplicates(num_frames, num_iterations)
print("Duplicate frame index:", duplicate_index)