"""
Molecule class for molecule_project.

A Molecule is a collection of Atom objects and supports:
- loading from an XYZ file
- translating the molecule
- rotating the molecule
- stretching a bond
- rotating a dihedral angle
"""

from .atom import Atom
import numpy as np


class Molecule:
    def __init__(self, atoms=None):
        self.atoms = atoms if atoms is not None else []

    # ---------------------------
    # BASIC OPERATIONS
    # ---------------------------
    def add_atom(self, atom: Atom):
        """Add a single Atom object to the molecule."""
        self.atoms.append(atom)

    def from_xyz(self, filename):
        """
        Load atoms from an XYZ file.
        Assumes standard XYZ format:
            N
            comment line
            symbol x y z
            ...
        """
        with open(filename, "r") as f:
            lines = f.readlines()

        # Skip first two lines
        coord_lines = lines[2:]

        for line in coord_lines:
            parts = line.split()
            if len(parts) < 4:
                continue
            symbol = parts[0].lower()
            x, y, z = map(float, parts[1:4])
            self.add_atom(Atom(symbol=symbol, coords=(x, y, z)))

        return self

    def get_coords(self):
        """Return Nx3 numpy array of atomic coordinates."""
        return np.array([a.coords for a in self.atoms])

    def set_coords(self, new_coords):
        """Write new coordinates back to Atom objects."""
        for atom, c in zip(self.atoms, new_coords):
            atom.set_coords(*c)

    # ---------------------------
    # TRANSLATION
    # ---------------------------
    def translate(self, vector):
        """Translate molecule by given 3D vector."""
        vector = np.array(vector)
        new = self.get_coords() + vector
        self.set_coords(new)

    # ---------------------------
    # ROTATION
    # ---------------------------
    def rotate(self, origin=(0, 0, 0), axis=(0, 0, 1), angle_deg=0):
        """
        Rotate molecule around an arbitrary axis using Rodrigues' rotation formula.

        Parameters
        ----------
        origin : tuple
            Axis passes through this point
        axis : tuple
            Rotation axis direction
        angle_deg : float
            Rotation angle in degrees
        """
        origin = np.array(origin)
        axis = np.array(axis)
        axis = axis / np.linalg.norm(axis)
        angle = np.radians(angle_deg)

        coords = self.get_coords()
        shifted = coords - origin

        # Rodrigues rotation
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        k = axis

        rotated = (
            shifted * cos_a
            + np.cross(k, shifted) * sin_a
            + k * (np.dot(shifted, k)[:, None] * (1 - cos_a))
        )

        self.set_coords(rotated + origin)

    # ---------------------------
    # STRETCH A BOND
    # ---------------------------
    def stretch_bond(self, i, j, delta):
        """
        Stretch bond between atom i and j by delta Å.
        Moves only atom j (simple homework version).
        """
        coords = self.get_coords().copy()
        vec = coords[j] - coords[i]
        unit = vec / np.linalg.norm(vec)
        coords[j] += unit * delta
        self.set_coords(coords)

    # ---------------------------
    # ROTATE DIHEDRAL ANGLE
    # ---------------------------
    def rotate_dihedral(self, a, b, c, d, angle_deg):
        """
        Rotate dihedral angle defined by atoms a-b-c-d.
        Simplified homework version:
        - Axis is b -> c
        - Rotate only atom d and any atoms after it
        """
        coords = self.get_coords()
        p_b = coords[b]
        p_c = coords[c]
        axis = p_c - p_b

        # Which atoms to rotate?
        rot_indices = [i for i in range(d, len(self.atoms))]

        # Rotate selected atoms
        origin = p_b
        for idx in rot_indices:
            self.rotate(origin=origin, axis=axis, angle_deg=angle_deg,)

    def __repr__(self):
        return f"Molecule with {len(self.atoms)} atoms"

