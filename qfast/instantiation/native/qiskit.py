"""
This module implements qiskit's isometry decomposition
as a native tool plugin to QFAST.
"""

import qiskit

from qfast import utils
from qfast.instantiation import nativetool


class QiskitTool ( nativetool.NativeTool ):
    """Synthesize tool built on QISKit's Isometry Decomposition."""

    def get_maximum_size ( self ):
        """
        The maximum size of a unitary matrix (in qubits) that can be
        decomposed with this tool.

        Returns:
            (int): The qubit count this tool can handle.
        """

        # Larger unitaries can be decomposed with this tool,
        # however, solution quality is best at 3 qubits.
        return 3

    def synthesize ( self, utry ):
        """
        Synthesis function with this tool.

        Args:
            utry (np.ndarray): The unitary to synthesize.

        Returns
            qasm (str): The synthesized QASM output.

        Raises:
            TypeError: If utry is not a valid unitary.

            ValueError: If the utry has invalid dimensions.
        """

        if not utils.is_unitary( utry, tol = 1e-14 ):
            raise TypeError( "utry must be a valid unitary." )

        if utry.shape[0] > 2 ** self.get_maximum_size():
            raise ValueError( "utry has incorrect dimensions." )

        num_qubits = utils.get_num_qubits( utry )
        basis_gates = [ 'u1', 'u2', 'u3', 'cx', 'id' ]

        circ = qiskit.QuantumCircuit( num_qubits )
        circ.iso( utry, list( reversed( range( num_qubits ) ) ), [] )
        circ = qiskit.transpile( circ,
                                 optimization_level = 3,
                                 basis_gates = basis_gates )
        return circ.qasm()

