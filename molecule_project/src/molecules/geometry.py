"""
Geometry helper functions for molecule_project.

Provides:
- vector math utilities
- distance between atoms
- bond angle
- dihedral angle
- Rodrigues rotation for arbitrary-axis rotation
"""

import numpy as np


# ----------------------------
# Basic vector utilities
# ----------------------------

def v(x):
    """Convert tuple/list to numpy vector."""
    return np.array(x, dtype=float)


def normalize(vec):
    """Return normalized vector."""
    vec = np.array(vec, dtype=float)
    n = np.linalg.norm(vec)
    if n == 0:
        return vec
    return vec / n


def distance(a, b):
    """Distance between points a and b."""
    return np.linalg.norm(v(a) - v(b))


# ----------------------------
# Bond angle
# ----------------------------

def angle(a, b, c):
    """
    Bond angle (degrees) for atoms at coordinates a-b-c.
    b is the vertex.
    """
    v1 = v(a) - v(b)
    v2 = v(c) - v(b)
    v1 = normalize(v1)
    v2 = normalize(v2)
    cos_theta = np.clip(np.dot(v1, v2), -1.0, 1.0)
    return float(np.degrees(np.arccos(cos_theta)))


# ----------------------------
# Dihedral angle
# ----------------------------

def dihedral(a, b, c, d):
    """
    Dihedral angle (degrees) between atoms a-b-c-d.
    """
    p0 = v(a)
    p1 = v(b)
    p2 = v(c)
    p3 = v(d)

    b0 = p1 - p0
    b1 = p2 - p1
    b2 = p3 - p2

    b1_norm = normalize(b1)

    v = b0 - np.dot(b0, b1_norm) * b1_norm
    w = b2 - np.dot(b2, b1_norm) * b1_norm

    x = np.dot(normalize(v), normalize(w))
    y = np.dot(np.cross(b1_norm, normalize(v)), normalize(w))

    return float(np.degrees(np.arctan2(y, x)))


# ----------------------------
# Rodrigues rotation
# ----------------------------

def rodrigues_rotate(point, origin, axis, angle_deg):
    """
    Rotate a point around an axis passing through origin using Rodrigues' formula.

    Parameters
    ----------
    point : array-like
    origin : array-like
    axis : array-like (axis direction)
    angle_deg : float

    Returns
    -------
    rotated point as numpy array
    """
    p = v(point) - v(origin)
    k = normalize(axis)
    angle = np.radians(angle_deg)

    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    rotated = (
        p * cos_a
        + np.cross(k, p) * sin_a
        + k * np.dot(k, p) * (1 - cos_a)
    )

    return rotated + v(origin)

