import cirq
import numpy as np

def quantum_feature_map(data_point):
    """ Encodes stock data into a quantum circuit """
    qubits = [cirq.GridQubit(0, i) for i in range(len(data_point))]
    circuit = cirq.Circuit()

    for i, value in enumerate(data_point):
        circuit.append(cirq.rx(value * np.pi)(qubits[i]))

    return circuit

if __name__ == "__main__":
    test_data = [0.1, 0.5, 0.3, 0.7]  # Example stock data point
    print(quantum_feature_map(test_data))
