"""
Atom class for molecule_project

Atoms can be created by:
- symbol (string, e.g., "c", "o", "h")
- atomic number (z)

Each atom stores:
- symbol (lowercase string)
- atomic number z
- mass
- covalent (single-bond) radius
- double-bond radius (approximate values)
- 3D coordinates (x, y, z)
"""

# Minimal periodic table (extend later if needed)
_periodic_table = {
    "h":  {"z": 1,  "mass": 1.008,  "r_single": 0.31, "r_double": 0.0},
    "c":  {"z": 6,  "mass": 12.011, "r_single": 0.76, "r_double": 0.67},
    "n":  {"z": 7,  "mass": 14.007, "r_single": 0.71, "r_double": 0.60},
    "o":  {"z": 8,  "mass": 15.999, "r_single": 0.66, "r_double": 0.57},
    "s":  {"z": 16, "mass": 32.06,  "r_single": 1.05, "r_double": 0.94},
    "cl": {"z": 17, "mass": 35.45,  "r_single": 1.02, "r_double": 0.0},
}

# Convenience dicts
_symbol_to_z = {sym: data["z"] for sym, data in _periodic_table.items()}
_z_to_symbol = {data["z"]: sym for sym, data in _periodic_table.items()}


class Atom:
    def __init__(self, symbol=None, z=None, coords=(0.0, 0.0, 0.0)):
        """
        Create an Atom from symbol or atomic number.
        Coordinates default to (0,0,0).

        Example:
            Atom(symbol="c", coords=(0,0,0))
            Atom(z=8, coords=(1.0, 0.0, 0.0))
        """
        # Handle symbol or atomic number
        if symbol is None and z is None:
            raise ValueError("Provide either atomic symbol or atomic number (z).")

        if symbol is not None:
            symbol = symbol.lower()
            if symbol not in _periodic_table:
                raise KeyError(f"Unknown element symbol: {symbol}")
        else:
            # Determine symbol from atomic number
            if z not in _z_to_symbol:
                raise KeyError(f"Unknown atomic number: {z}")
            symbol = _z_to_symbol[z]

        data = _periodic_table[symbol]

        self.symbol = symbol
        self.z = data["z"]
        self.mass = data["mass"]
        self.r_single = data["r_single"]
        self.r_double = data["r_double"]

        # Set coordinates
        self.coords = tuple(float(c) for c in coords)

    def set_coords(self, x, y, z):
        """Update atom coordinates."""
        self.coords = (float(x), float(y), float(z))

    def __repr__(self):
        return (
            f"Atom(symbol='{self.symbol}', z={self.z}, "
            f"coords={self.coords})"
        )

