#!/usr/bin/env python

"""
Scripts which plots the inner ghost set up.
"""

import matplotlib.pyplot as plt
import numpy as np

font = {"family":"serif", "serif": ["computer modern roman"]}
titleSize = 25
size = 30
plt.rc("font", size = size)
plt.rc("axes", titlesize = titleSize)
plt.rc("font", **font)
plt.rc("text", usetex=True)

def plotInnerGhost(nx        =  4   ,\
                   dx        =  1   ,\
                   nz        =  8   ,\
                   outerBC   = True ,\
                   annotate  = True ,\
                   showPlot  = False,\
                   extension ="pdf"  ):
    """
    Plots the inner ghost set up

    Parameters
    ----------
    nx : int
        Number of points in rho
    dx : float
        Grid spacing in rho
    nz : int
        Number of points in theta
    outerBC: bool
        Whether or not to plot the outer boundary condition
    annotate: bool
        Whether or not to annotate
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

    fig = plt.figure(figsize=(12,12))
    ax  = fig.add_subplot(111)
    ax.set_axis_off()
    # Make grid
    rho = np.linspace(dx/2, (nx-0.5)*dx, nx)

    # Make the radii
    for radius in rho:
        curCircle = plt.Circle((0, 0), radius, color="k", lw=lw, fill=False)
        ax.add_artist(curCircle)

    eps = 0.5*dx
    if outerBC:
        # Ghost-point is 0.5 away from last inner
        xGhost = nx*dx
        rho = np.append(rho, xGhost)
        ghostCircle = plt.Circle((0, 0), xGhost, color="k", lw=lw, ls="--",\
                                 fill=False)
        ax.add_artist(ghostCircle)

        ax.set_xlim([-(xGhost+eps), (xGhost+eps)])
        ax.set_ylim([-(xGhost+eps), (xGhost+eps)])
    else:
        ax.set_xlim([-(rho[-1]+eps), (rho[-1]+eps)])
        ax.set_ylim([-(rho[-1]+eps), (rho[-1]+eps)])

    # Make the z lines
    theta = np.linspace(0, 2*np.pi, nz+1)
    # Exclude last point (only count this once)
    theta = theta[:-1]

    # Have the transformation
    # x = rho*np.cos(theta)
    # y = rho*np.sin(theta)
    for curTheta in theta:
        xStart = rho[0 ]*np.cos(curTheta)
        xEnd   = rho[-1]*np.cos(curTheta)
        yStart = rho[0 ]*np.sin(curTheta)
        yEnd   = rho[-1]*np.sin(curTheta)
        ax.plot((xStart, xEnd),(yStart, yEnd), lw=lw, color="k")

    # Make the cross in the center
    crossLength = dx/6
    ax.plot((-crossLength, crossLength),(0,0) , lw=lw, color="k")
    ax.plot((0,0), (-crossLength, crossLength), lw=lw, color="k")

    # Common point markers
    thetaInd = 1
    color    = "green"
    lwM      = lw*3.5
    radius   = dx*0.25
    zorder   = 10
    # Set inner point markers
    startTheta = theta[thetaInd]
    nPoints    = 3
    for i in range(nPoints):
        xStart = rho[i]*np.cos(startTheta)
        yStart = rho[i]*np.sin(startTheta)
        markerCircle = plt.Circle((xStart, yStart,), radius,\
                                  color=color, lw=lwM, fill=False,\
                                  zorder=zorder)
        ax.add_artist(markerCircle)

    # Set ghost-point markers
    endTheta = theta[int(len(theta)/2)+thetaInd]
    nPoints    = 2
    for i in range(nPoints):
        xStart = rho[i]*np.cos(endTheta)
        yStart = rho[i]*np.sin(endTheta)
        ghostMarkerCircle = plt.Circle((xStart, yStart,), radius,\
                color=color, lw=lwM, ls=":", fill=False,\
                         zorder=zorder)
        ax.add_artist(ghostMarkerCircle)

    # Annotate
    if annotate:
        # NOTE: Text on saved file may differ from plt.show()
        size  = 70
        place = rho[-1]*0.90
        ax.annotate(r"$\theta_i$",
                 xy=(place, place), xycoords='data',
                 xytext=(place, place), textcoords='data',
                 size=size, va="center", ha="center",
                 )

        ax.annotate(r"$\theta_i+\pi$",
                 xy=(-place, -place), xycoords='data',
                 xytext=(-place, -place), textcoords='data',
                 size=size, va="center", ha="center",
                 )

    ax.set_aspect("equal")

    fig.tight_layout()
    fileName = "../innerGhost.{}".format(extension)
    fig.savefig(fileName, transparent=True)
    if showPlot:
        plt.show()

    return fileName

if __name__ == "__main__":
    from subprocess import Popen
    fileName = plotInnerGhost()
    # Crop with pdfCrop
    Popen("pdfcrop {0} {0}".format(fileName), shell=True).wait()
