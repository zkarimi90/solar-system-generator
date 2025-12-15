"""
checkpoint.py — save and load molecule checkpoints using HDF5.

Defines:
    IOData  — class to save/load molecular data
"""

from pathlib import Path
import h5py
import numpy as np


class IOData:
    """
    IOData handles reading and writing checkpoint files.

    A checkpoint file stores:
        - atomic symbols
        - atomic coordinates
    """

    def __init__(self, options=None):
        self.options = options if options is not None else {}

    def write_checkpoint_file(self, filename, molecule):
        """
        Save a Molecule object to an HDF5 checkpoint file.

        Parameters
        ----------
        filename : str or Path
        molecule : Molecule object
        """
        filename = Path(filename)

        symbols = np.array([a.symbol for a in molecule.atoms], dtype="S4")
        coords = np.array([a.coords for a in molecule.atoms], dtype=float)

        with h5py.File(filename, "w") as f:
            f.create_dataset("symbols", data=symbols)
            f.create_dataset("coords", data=coords)

        print("Checkpoint saved to", filename)

    def read_checkpoint_file(self, filename):
        """
        Load a Molecule from an HDF5 checkpoint file.

        Returns:
            Molecule object
        """
        from molecules.atom import Atom
        from molecules.molecule import Molecule

        filename = Path(filename)

        with h5py.File(filename, "r") as f:
            symbols = [s.decode("utf-8") for s in f["symbols"][()]]
            coords = f["coords"][()]

        mol = Molecule()
        for sym, xyz in zip(symbols, coords):
            mol.add_atom(Atom(symbol=sym, coords=xyz))

        print("Checkpoint loaded from", filename)
        return mol

