import cirq
cx_pattern = "11001"
n = len(cx_pattern)
myqubits = cirq.LineQubit.range(n+1)
print(myqubits)
cx_qubits = [myqubits[x] for x in range(n) if cx_pattern[x] == "1"]
target_qubit = myqubits[-1]

mycircuit = cirq.Circuit(
    [
        cirq.reset_each(*myqubits),
        cirq.X(target_qubit),
        cirq.Moment(cirq.H.on_each(myqubits)),
        cirq.CNOT.on_each(zip(cx_qubits, [target_qubit]*len(cx_qubits))),
        cirq.Moment(cirq.H.on_each(myqubits))
    ]
)


meas_gates = cirq.Moment([cirq.measure(qubit) for qubit in myqubits])
mycircuit.append(meas_gates)

#now simulate 
sim = cirq.Simulator()
result= sim.run(mycircuit, repetitions=2)

print(result)
print(mycircuit)
