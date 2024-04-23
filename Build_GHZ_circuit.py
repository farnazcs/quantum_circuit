import cirq

def make_GHZ(num_qubits, measurements = True):
  myqubits = cirq.LineQubit.range(num_qubits)
  GHZ_circuit = cirq.Circuit([
      cirq.Moment([cirq.H(myqubits[0])])
  ])

  for x in range(num_qubits-1):
    GHZ_circuit.append(cirq.CNOT(myqubits[x], myqubits[x+1]))

  if measurements:
    GHZ_circuit.append(cirq.Moment(cirq.measure_each(*myqubits)))

  return GHZ_circuit



GHZ_5q = make_GHZ(5)

print("this is GHZ 5 qubits circuit: ")
print(GHZ_5q)
