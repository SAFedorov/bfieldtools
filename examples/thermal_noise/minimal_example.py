"""
Minimal example
=================

"""
import numpy as np
import matplotlib.pyplot as plt
import trimesh


from bfieldtools.thermal_noise import (
    compute_AC_current_modes,
    compute_DC_current_modes,
)

import pkg_resources


font = {"family": "normal", "weight": "normal", "size": 16}
plt.rc("font", **font)

# Fix the simulation parameters
d = 100e-6
sigma = 3.7e7
T = 300
kB = 1.38064852e-23
mu0 = 4 * np.pi * 1e-7
freqs = np.array((0,))


Nchunks = 8
quad_degree = 2


mesh = trimesh.load(
    pkg_resources.resource_filename("bfieldtools", "example_meshes/unit_sphere.stl")
)


freqs = np.array((0,))

vl = compute_DC_current_modes(mesh, T=T, resistivity=1e-7, thickness=1e-3)
vl = compute_AC_current_modes(mesh, freqs, T=T, resistivity=1e-7, thickness=1e-3)


mesh = trimesh.load(
    pkg_resources.resource_filename("bfieldtools", "example_meshes/unit_disc.stl")
)


freqs = np.array((0,))

vl_open = compute_DC_current_modes(mesh, T=T, resistivity=1e-7, thickness=1e-3)
vl_open = compute_AC_current_modes(mesh, freqs, T=T, resistivity=1e-7, thickness=1e-3)


mesh = trimesh.load(
    pkg_resources.resource_filename("bfieldtools", "example_meshes/plane_w_holes.stl")
)


freqs = np.array((0,))

vl_openh = compute_DC_current_modes(mesh, T=T, resistivity=1e-7, thickness=1e-3)
vl_openh = compute_AC_current_modes(mesh, freqs, T=T, resistivity=1e-7, thickness=1e-3)