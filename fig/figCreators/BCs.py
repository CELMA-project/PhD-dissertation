#!/usr/bin/env python

"""
Scripts which plots the boundary conditions.
"""

import copy
import matplotlib.pyplot as plt
import numpy as np

font = {"family":"serif", "serif": ["computer modern roman"]}
titleSize = 25
size = 30
plt.rc("font", size = size)
plt.rc("axes", titlesize = titleSize)
plt.rc("font", **font)
plt.rc("text", usetex=True)

def plotBCs(showPlot  = False,\
            extension ="pdf"  ):
    """
    Plots the boundary conditions

    Parameters
    ----------
    showPlot: bool
        Whether or not to show the plot
    extension: str
        Extension of the plot to save

    Returns
    -------
    fileName : str
        The name of the saved file
    """

    lw = 2

    fig, (stagAx, radiAx, sheathAx) = plt.subplots(ncols=3,
            figsize=(18,12))

    stagAx  .set_title("Boundary conditions for\nthe stagnation point")
    radiAx  .set_title("Boundary conditions for\nthe outer radius")
    sheathAx.set_title("Boundary conditions for\nthe sheath entrance")
    stagAx  .set_axis_off()
    radiAx  .set_axis_off()
    sheathAx.set_axis_off()

    # Make circles and rectangle
    circ = plt.Circle((0.0, 0.0,), 1.0,\
                     color="black", lw=2.0, fill=False,\
                     zorder=10)
    rect = plt.Rectangle((-0.5, -1.0,), 1.0, 2.0,\
                     color="black", lw=2.0, fill=False,\
                     zorder=10)
    stagCirc   = copy.copy(circ)
    sheathCirc = copy.copy(circ)
    stagAx  .add_artist(stagCirc)
    radiAx  .add_artist(rect)
    sheathAx.add_artist(sheathCirc)
    eps = 0.05
    lim = 1 + eps
    stagAx  .set_xlim([-lim, lim])
    radiAx  .set_xlim([-(0.5+eps), (0.5+eps)])
    sheathAx.set_xlim([-lim, lim])
    stagAx  .set_ylim([-lim, lim])
    radiAx  .set_ylim([-lim, lim])
    sheathAx.set_ylim([-lim, lim])

    # Specify BC
    stagBC =   (
                r"$\partial_\| n = 0$""\n"
                r"$u_{e, \|} = 0$""\n"
                r"$u_{i, \|} = 0$""\n"
                r"$\partial_\| \Omega = 0$""\n"
                r"$\phi$ is extrapolated"
               )
    radiBC =   (
                r"$\partial_\rho n = 0$""\n"
                r"$\partial_\rho u_{e, \|} = 0$""\n"
                r"$\partial_\rho u_{i, \|} = 0$""\n"
                r"$\partial_\rho \Omega = 0$""\n"
                r"$\phi=0$"
               )
    sheathBC = (
                r"$\partial_\| n = 0$""\n"
                r"$u_{e, \|} = c_se^{"
                    r"\left(\Lambda+\frac{e[\phi_0+\phi]}{T_e}\right)}$""\n"
                r"$u_{i, \|} = c_s$""\n"
                r"$\partial_\| \Omega = 0$""\n"
                r"$\phi$ is extrapolated"
               )

    # Annotate
    # NOTE: Text on saved file may differ from plt.show()
    size = 30
    stagAx.  annotate(stagBC,
             xy=(0, 0), xycoords='data',
             xytext=(0, 0), textcoords='data',
             size=size, va="center", ha="center",
             )
    radiAx.  annotate(radiBC,
             xy=(0, 0), xycoords='data',
             xytext=(0, 0), textcoords='data',
             size=size, va="center", ha="center",
             )
    sheathAx.annotate(sheathBC,
             xy=(0, 0), xycoords='data',
             xytext=(0, 0), textcoords='data',
             size=size, va="center", ha="center",
             )

    stagAx  .set_aspect("equal")
    radiAx  .set_aspect("equal")
    sheathAx.set_aspect("equal")

    # fig.tight_layout()
    fileName = "../BCs.{}".format(extension)
    fig.savefig(fileName, transparent=True)
    if showPlot:
        plt.show()

    return fileName

if __name__ == "__main__":
    from subprocess import Popen
    fileName = plotBCs()
    # Crop with pdfCrop
    Popen("pdfcrop {0} {0}".format(fileName), shell=True).wait()
