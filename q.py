import qiskit
print(qiskit.__version__)

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2)
qc.h(0)        # Hadamard: qubit 0 in superpositie
qc.cx(0, 1)    # CNOT: verstrengelt qubit 1 met qubit 0
qc.measure_all()

print(qc.draw())

sampler = StatevectorSampler()
result = sampler.run([qc], shots=1000).result()
counts = result[0].data.meas.get_counts()
print(counts)