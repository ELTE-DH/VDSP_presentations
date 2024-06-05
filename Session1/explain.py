import fdtd
import numpy as np
import matplotlib.pyplot as plt

# Set the backend to numpy
fdtd.set_backend("numpy")


# Init simulation grid
grid = fdtd.Grid(
    shape = (25e-6, 15e-6, 1), # 25um x 15um x 1 (grid_spacing) --> 2D FDTD
)

print(grid)

# Add two objects
grid[11:32, 30:84, 0] = fdtd.Object(permittivity=1.7**2, name="object")

print(grid.object)

grid[13e-6:18e-6, 5e-6:8e-6, 0] = fdtd.Object(permittivity=1.5**2)

print(grid.objects)

# Add source
grid[7.5e-6:8.0e-6, 11.8e-6:13.0e-6, 0] = fdtd.LineSource(
    period = 1550e-9 / (3e8), name="source"
)

print(grid.source)

# Add detector
grid[12e-6, :, 0] = fdtd.LineDetector(name="detector")
print(grid.detector)

# Add grid boundaries
# x boundaries
# grid[0, :, :] = fdtd.PeriodicBoundary(name="xbounds")
grid[0:10, :, :] = fdtd.PML(name="pml_xlow")
grid[-10:, :, :] = fdtd.PML(name="pml_xhigh")

# y boundaries
# grid[:, 0, :] = fdtd.PeriodicBoundary(name="ybounds")
grid[:, 0:10, :] = fdtd.PML(name="pml_ylow")
grid[:, -10:, :] = fdtd.PML(name="pml_yhigh")


print(grid)

# Run simulation
grid.run(total_time=100)

# Plot the detector data
plt.figure()
plt.ylabel("|E|")
plt.xlabel("Time step")
plt.title("Detected E field absolute value summed over the whole detector over time")
plt.plot(np.sum(np.linalg.norm(grid.detectors[0].detector_values()["E"],axis=2),axis=1))

# Visualize the grid
plt.figure()
grid.visualize(z=0, show=False)

plt.show()