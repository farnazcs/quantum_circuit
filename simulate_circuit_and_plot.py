import cirq

def get_circuit(resete = False, measurements = False):
      cx_pattern = "11001"
 
      n = len(cx_pattern)
      myqubits = cirq.LineQubit.range(n+1)
      #print(myqubits)
      cx_qubits = [myqubits[x] for x in range(n) if cx_pattern[x] == "1"]
      target_qubit = myqubits[-1]

      mycircuit = cirq.Circuit()

      if resete:
        mycircuit.append([cirq.reset(qubit) for qubit in myqubits]),

      mycircuit.append(

        [
          cirq.reset_each(*myqubits),
          cirq.X(target_qubit),
          cirq.Moment(cirq.H.on_each(myqubits)),
          cirq.CNOT.on_each(zip(cx_qubits, [target_qubit]*len(cx_qubits))),
          cirq.Moment(cirq.H.on_each(myqubits))
        ],
      )
    
      if measurements:
        mycircuit.append(cirq.Moment(cirq.measure(*myqubits[:-1], key = "meas_qubits")))

      return mycircuit


circuit_without_reset_measurements = get_circuit(resete= False, measurements= False)
circuit_with_reset_measurements = get_circuit(resete= True, measurements= True)
print("circuit without reset measurement:")
print(circuit_without_reset_measurements)
print("circuit with reset measurements:")
print(circuit_with_reset_measurements)


#now simulate
sim = cirq.Simulator()
result = sim.run(circuit_with_reset_measurements, repetitions= 50)
print("results :")
print(result)


cirq.plot_state_histogram(result)

