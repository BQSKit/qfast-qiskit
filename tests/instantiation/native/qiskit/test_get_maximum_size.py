import numpy    as np
import unittest as ut

from qfast.instantiation.native.qiskit import QiskitTool


class TestQiskitGetMaximumSize ( ut.TestCase ):

    def test_qiskit_get_maximum_size ( self ):
        qtool = QiskitTool()
        block_size = qtool.get_maximum_size()
        self.assertEqual( block_size, 3 )


if __name__ == '__main__':
    ut.main()
