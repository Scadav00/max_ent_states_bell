# -*- coding: utf-8 -*-

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(7, 'q')
creg_c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.rz(pi / 2, qreg_q[3])
circuit.sx(qreg_q[3])
circuit.rz(pi, qreg_q[3])
circuit.cx(qreg_q[3], qreg_q[1])
circuit.sx(qreg_q[3])
circuit.rz(pi / 2, qreg_q[3])
circuit.measure(qreg_q[3], creg_c[0])