import cirq
import numpy as np

class MyGate(cirq.Gate):
    def __init__(self, k):
        super().__init__()
        self.k = k

    # Define the number of qubits this gate acts on
    def _num_qubits_(self):
        return 2

    # Define the shape of the quantum state vector after applying this gate
    def _qid_shape_(self):
        return (2,) * self.num_qubits()

    # Define the unitary matrix representing this gate
    def _unitary_(self):
        return np.array([
                     [1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,0],
                     [0,0,0,np.exp(2*np.pi*1j/(2**self.k))]
                         ])
  
    # Define additional info to build the gate, e.g., for circuit diagram
    def _circuit_diagram_info_(self, args):
         return "Ctrl", "Target"

mygate = MyGate(k = 1)

myqubit = cirq.LineQubit.range(2)
mycircuit = cirq.Circuit(mygate(*myqubit))
print(mycircuit)
unit_matrix = cirq.unitary(mycircuit)
print(unit_matrix)
