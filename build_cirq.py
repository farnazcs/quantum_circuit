import cirq
#creat 6 qubits
myqubits = cirq.LineQubit.range(6)
mycircuit = cirq.Circuit()

#reset all of them to state 0, in a for loop, and creat the moment for that set of the reset
reset_qubits = cirq.Moment([cirq.reset(qubit) for qubit in myqubits])
type(reset_qubits)

#append that moment to the circuit
mycircuit.append(reset_qubits)

#flip the last qubit to state 1
setup_detect_qubit = cirq.X(myqubits[-1])

#now append that to the circuit 
mycircuit.append(setup_detect_qubit)

#add H gate, and append a moment
H_gates = cirq.Moment(cirq.H.on_each(myqubits))
mycircuit.append(H_gates)

#for cNOT gates: 
mycircuit.append([
                  cirq.CNOT(myqubits[4], myqubits[5]),
                  cirq.CNOT(myqubits[1], myqubits[5]),
                  cirq.CNOT(myqubits[0], myqubits[5])
])

mycircuit.append(H_gates)

#now add measurement at the end

meas_gates = cirq.Moment([cirq.measure(qubit) for qubit in myqubits])
mycircuit.append(meas_gates)

#now simulate 
sim = cirq.Simulator()
result= sim.run(mycircuit)

print(result)
print(mycircuit)
