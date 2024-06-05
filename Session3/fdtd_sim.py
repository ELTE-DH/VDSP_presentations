import fdtd
from taskweaver.plugin import Plugin, register_plugin
import matplotlib.pyplot as plt
import numpy as np
import PIL

@register_plugin
class FDTDPlugin(Plugin):
    def __call__(self, gridx, gridy, detector, objects, sources, pml_width, total_time):
        """
        This function runs a 2D Electromagnetic Finite-Difference Time-Domain (FDTD) simulation on the provided grid.
        :param gridx: the x dimension of the grid in um.
        :param gridy: the y dimension of the grid in um.
        :param detector: a detector object with {name: str, variable: {e:bool, h:bool} type: str(line, current, block), xrange: tuple, yrange: tuple} if a tuple element is None it will be a line detector, if both tupple elements are None a full grid segment is used. Ranges are in meters.
        :param objects: a list of objects with {permittivity: float, name: str, xrange: tuple, yrange: tuple}. Ranges are in meters.
        :param sources: a list of sources with {name: str, type:str(line, point), xrange: tuple, yrange: tuple, period: float, amplitude: float}. Ranges are in meters.
        :param pml_width: the width of the perfectly matched layer boundary in um from the edges of the grid.
        :param total_time: the total time of the simulation in seconds.

        :return: the detected E field, H field and the grid images as 3 separate PIL images.
        """
        # Run simulation
        fdtd.set_backend("numpy")

        # Init simulation grid
        grid = fdtd.Grid(
            shape=(gridx, gridy, 1),  # 2D FDTD
        )

        # Add objects
        for obj in objects:
            grid[obj["xrange"][0]:obj["xrange"][1], obj["yrange"][0]:obj["yrange"][1], 0] = fdtd.Object(
                permittivity=obj["permittivity"], name=obj["name"]
            )

        # Add sources
        for src in sources:
            if src["type"] == "line":
                grid[src["xrange"][0]:src["xrange"][1], src["yrange"][0]:src["yrange"][1], 0] = fdtd.LineSource(
                    period=src["period"], amplitude=src["amplitude"], name=src["name"]
                )
            elif src["type"] == "point":
                grid[src["xrange"][0]:src["xrange"][1], src["yrange"][0]:src["yrange"][1], 0] = fdtd.PointSource(
                    period=src["period"], amplitude=src["amplitude"], name=src["name"]
                )
            else:
                raise ValueError("Source type not supported, please use 'line' or 'point'")

        # Add detector
        if detector["type"] == "line":
            grid[detector["xrange"][0]:detector["xrange"][1], detector["yrange"][0]:detector["yrange"][1], 0] = fdtd.LineDetector(
                name=detector["name"]
            )
        elif detector["type"] == "current":
            grid[detector["xrange"][0]:detector["xrange"][1], detector["yrange"][0]:detector["yrange"][1], 0] = fdtd.CurrentDetector(
                name=detector["name"]
            )
        elif detector["type"] == "block":
            grid[detector["xrange"][0]:detector["xrange"][1], detector["yrange"][0]:detector["yrange"][1], 0] = fdtd.BlockDetector(
                name=detector["name"]
            )
        else:
            raise ValueError("Detector type not supported, please use 'line', 'current' or 'block'")

        # Add grid boundaries
        grid[0:pml_width, :, :] = fdtd.PML(name="pml_xlow")
        grid[-pml_width:, :, :] = fdtd.PML(name="pml_xhigh")
        grid[:, 0:pml_width, :] = fdtd.PML(name="pml_ylow")
        grid[:, -pml_width:, :] = fdtd.PML(name="pml_yhigh")

        grid.run(total_time=total_time)

        # Plot the detector data
        plt.figure()
        plt.ylabel("|E|")
        plt.xlabel("Time step")
        plt.title("Detected E field absolute value summed over the whole detector over time")
        plt.plot(np.sum(np.linalg.norm(grid.detectors[0].detector_values()["E"], axis=2), axis=1))


        plt.savefig("detected_e_field.png", bbox_inches="tight")
        imge = PIL.Image.open("detected_e_field.png")


        # The same for H

        plt.figure()
        plt.ylabel("|H|")
        plt.xlabel("Time step")
        plt.title("Detected H field absolute value summed over the whole detector over time")
        plt.plot(np.sum(np.linalg.norm(grid.detectors[0].detector_values()["H"], axis=2), axis=1))

        plt.savefig("detected_h_field.png", bbox_inches="tight")
        imgh = PIL.Image.open("detected_h_field.png")

        # Visualize the grid
        plt.figure()
        grid.visualize(z=0, show=False)

        plt.savefig("grid.png", bbox_inches="tight")
        imgg = PIL.Image.open("grid.png")

        return imge, imgh, imgg