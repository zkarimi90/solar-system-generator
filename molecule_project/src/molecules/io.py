"""
io.py — read/write XYZ files for molecule_project
"""

from .atom import Atom


def read_xyz(filename):
    """
    Read an XYZ file and return a list of Atom objects.

    Expected XYZ format:
        N
        comment
        symbol  x  y  z
        ...
    """
    atoms = []

    with open(filename, "r") as f:
        lines = f.readlines()

    if len(lines) < 2:
        raise ValueError("Invalid XYZ file: too few lines.")

    # Ignore the first two lines (atom count + comment)
    data_lines = lines[2:]

    for line in data_lines:
        parts = line.split()
        if len(parts) < 4:
            continue

        symbol = parts[0].lower()   # lowercase for consistency
        x, y, z = map(float, parts[1:4])

        atoms.append(Atom(symbol=symbol, coords=(x, y, z)))

    return atoms


def write_xyz(filename, atoms, comment="Written by molecule_project"):
    """
    Write an XYZ file from a list of Atom objects.
    """
    with open(filename, "w") as f:
        f.write(f"{len(atoms)}\n")
        f.write(comment + "\n")
        for atom in atoms:
            x, y, z = atom.coords
            f.write(f"{atom.symbol} {x:.6f} {y:.6f} {z:.6f}\n")

