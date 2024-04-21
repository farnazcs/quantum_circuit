#This is the class template that we can use
import cirq
import numpy as np

class MyGate(cirq.Gate):
    def __init__(self):
        super().__init__()

    # Define the number of qubits this gate acts on
    def _num_qubits_(self):
        return 1

    # Define the shape of the quantum state vector after applying this gate
    def _qid_shape_(self):
        return (2,) * self.num_qubits()

        # Define additional info to build the gate, e.g., for circuit diagram
    def _circuit_diagram_info_(self, args):
        return 'MyGate'
