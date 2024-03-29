# Deprecation

QFAST is no longer being actively maintained.  The successor to QFAST is [BQSKit](https://github.com/BQSKit/bqskit).

BQSKit combines several quantum synthesis projects, including the main synthesis algorithm implemented by QFAST, [qsearch](https://github.com/BQSKit/qfast), and a circuit partitioning and reoptimization project. BQSKit is being actively developed and with new features and bug fixes, including updates based on feedback from users.

BQSKit does have a different API, so moving an existing project to BQSKit may take some effort. In the meantime, qfast isn't going anywhere, but is not longer actively maintained, will not receive any new features, and may not receive bugfix or compatability updates.

# QFAST-QISKit: QISKit Plugin for QFAST

QFAST-QISKit packages several QISKit tools for [QFAST](https://github.com/BQSKit/qfast).
There are two native tools, KAKTool and QiskitTool, that are included.
Also, QiskitCombiner is a recombination tool that uses qiskit to
piece together small circuits. The QiskitCombiner provides circuit optimization
that isn't available with the default NaiveCombiner.

## Installation

The best way to install this python package is with pip.

```
pip install qfast-qiskit
```

## Copyright

Quantum Fast Approximate Synthesis Tool (QFAST) Copyright (c) 2020,
The Regents of the University of California, through Lawrence Berkeley
National Laboratory (subject to receipt of any required approvals from
the U.S. Dept. of Energy). All rights reserved.

If you have questions about your rights to use or distribute this software,
please contact Berkeley Lab's Intellectual Property Office at
IPO@lbl.gov.

NOTICE.  This Software was developed under funding from the U.S. Department
of Energy and the U.S. Government consequently retains certain rights.  As
such, the U.S. Government has been granted for itself and others acting on
its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the
Software to reproduce, distribute copies to the public, prepare derivative 
works, and perform publicly and display publicly, and to permit others to do so.

