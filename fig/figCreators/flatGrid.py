#!/usr/bin/env python

"""
Scripts which plots the flat grid.
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

def plotFlatGrid(showPlot  = False,\
                 extension ="pdf"  ):
    """
    Plots the flat grid

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

    lw                    = 3
    lwMeasures            = 1.5
    numPoints             = 7
    lDotsAt               = 4
    xLen                  = 3.0
    yLen                  = 0.5
    halfHeightBC          = 0.1
    numberHeigth          = 0.2
    xEps                  = 0.1
    yEps                  = 0.05
    markersize            = 30
    annotationHeigthBC    = -(numberHeigth + 0.01)
    measureHeigthBC       = annotationHeigthBC + 0.07
    BCAnnotateHeigth      = annotationHeigthBC - 0.2
    measureEps            = 0.01
    # NOTE: Text on saved file may differ from plt.show()
    pointSize    = 40
    numberSize   = 30
    annotateSize = 30

    fig, ax = plt.subplots(figsize=(18,12))

    ax.set_axis_off()
    pointLine = np.linspace(0, xLen, numPoints)
    bc1 = (pointLine[1 ] - pointLine[0])/2.0
    bc2 = pointLine[-2] + bc1

    # Annotate
    lDots = r"$\ldots$"
    # Make the inner points and the ghosts
    ax.plot((pointLine[0]),(0), "kx", markerfacecolor="none",\
             ms=markersize, mew=lw)

    for point in pointLine[1:lDotsAt]:
        ax.plot((point),(0), "ko", markerfacecolor="none",\
                 ms=markersize, mew=lw)

    ax.annotate(lDots,
             xy=(pointLine[lDotsAt], 0), xycoords='data',
             xytext=(pointLine[lDotsAt], 0), textcoords='data',
             size=pointSize, va="center", ha="center",
             )

    for point in pointLine[lDotsAt+1:-1]:
        ax.plot((point),(0), "ko", markerfacecolor="none",\
                 ms=markersize, mew=lw)

    ax.plot((pointLine[-1]),(0), "kx", markerfacecolor="none",\
             ms=markersize, mew=lw)

    # Make the BCs
    ax.plot((bc1, bc1), (BCAnnotateHeigth + 2.5*yEps, halfHeightBC), "k--", lw=lw)
    ax.plot((bc2, bc2), (BCAnnotateHeigth + 2.5*yEps, halfHeightBC), "k--", lw=lw)
    ax.annotate("First\nboundary",
                xy=(bc1, BCAnnotateHeigth), xycoords='data',
                xytext=(bc1, BCAnnotateHeigth), textcoords='data',
                size=numberSize, va="center", ha="center",
                )
    ax.annotate("Last\nboundary",
                xy=(bc2, BCAnnotateHeigth), xycoords='data',
                xytext=(bc2, BCAnnotateHeigth), textcoords='data',
                size=numberSize, va="center", ha="center",
                )

    # Make the numbers (range excludes the last point)
    for i in range(numPoints-3):
        text = "Inner point\nwith index\n{}".format(i) if i > 0 else "Ghost point\nwith index\n{}".format(i)
        ax.annotate(text,
                    xy=(pointLine[i], numberHeigth), xycoords='data',
                    xytext=(pointLine[i], numberHeigth), textcoords='data',
                    size=numberSize, va="center", ha="center",
                    )

    ax.annotate("Inner point\nwith index\nN",
                xy=(pointLine[-2], numberHeigth), xycoords='data',
                xytext=(pointLine[-2], numberHeigth), textcoords='data',
                size=numberSize, va="center", ha="center",
                )

    ax.annotate("Ghost point\nwith index\nN+1",
                xy=(pointLine[-1], numberHeigth), xycoords='data',
                xytext=(pointLine[-1], numberHeigth), textcoords='data',
                size=numberSize, va="center", ha="center",
                )

    # Make the Delta
    # First BC segment
    halfBetween0AndBC = (bc1-pointLine[0])/2
    # Line
    ax.plot((pointLine[0]+measureEps, bc1-measureEps),\
            (measureHeigthBC, measureHeigthBC), "k", lw=lwMeasures)
    # Left tick
    ax.plot(((pointLine[0]+measureEps), (pointLine[0]+measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    # Rigth tick
    ax.plot(((bc1-measureEps), (bc1-measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    ax.annotate(r"$\Delta/2$",
                xy=(halfBetween0AndBC, annotationHeigthBC), xycoords='data',
                xytext=(halfBetween0AndBC, annotationHeigthBC), textcoords='data',
                size=annotateSize, va="center", ha="center",
                )

    # Second BC segment
    halfBetween1AndBC = bc1 + (pointLine[1]-bc1)/2
    # Line
    ax.plot((bc1+measureEps, pointLine[1]-measureEps),\
            (measureHeigthBC, measureHeigthBC), "k", lw=lwMeasures)
    # Left tick
    ax.plot(((bc1+measureEps), (bc1+measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    # Rigth tick
    ax.plot(((pointLine[1]-measureEps), (pointLine[1]-measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    ax.annotate(r"$\Delta/2$",
                xy=(halfBetween1AndBC, annotationHeigthBC), xycoords='data',
                xytext=(halfBetween1AndBC, annotationHeigthBC), textcoords='data',
                size=annotateSize, va="center", ha="center",
                )

    for i in range(2, lDotsAt):
        # Inner segment
        halfBetweenPoints = pointLine[i-1] + (pointLine[i]-pointLine[i-1])/2
        # Line
        ax.plot((pointLine[i-1]+measureEps, pointLine[i]-measureEps),\
                (measureHeigthBC, measureHeigthBC), "k", lw=lwMeasures)
        # Left tick
        ax.plot(((pointLine[i-1]+measureEps), (pointLine[i-1]+measureEps)),\
                (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
        # Rigth tick
        ax.plot(((pointLine[i]-measureEps), (pointLine[i]-measureEps)),\
                (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
        ax.annotate(r"$\Delta$",
                    xy=(halfBetweenPoints, annotationHeigthBC), xycoords='data',
                    xytext=(halfBetweenPoints, annotationHeigthBC), textcoords='data',
                    size=annotateSize, va="center", ha="center",
                    )

    # Secon last BC segment
    halfBetweenNAndBC = pointLine[-2] + (bc2-pointLine[-2])/2
    # Line
    ax.plot((pointLine[-2]+measureEps, bc2-measureEps),\
            (measureHeigthBC, measureHeigthBC), "k", lw=lwMeasures)
    # Left tick
    ax.plot(((pointLine[-2]+measureEps), (pointLine[-2]+measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    # Rigth tick
    ax.plot(((bc2-measureEps), (bc2-measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    ax.annotate(r"$\Delta/2$",
                xy=(halfBetweenNAndBC, annotationHeigthBC), xycoords='data',
                xytext=(halfBetweenNAndBC, annotationHeigthBC), textcoords='data',
                size=annotateSize, va="center", ha="center",
                )

    # Last BC segment
    halfBetweenBCAndNP1 = bc2 + (pointLine[-1]-bc2)/2
    # Line
    ax.plot((bc2+measureEps, pointLine[-1]-measureEps),\
            (measureHeigthBC, measureHeigthBC), "k", lw=lwMeasures)
    # Left tick
    ax.plot(((bc2+measureEps), (bc2+measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    # Rigth tick
    ax.plot(((pointLine[-1]-measureEps), (pointLine[-1]-measureEps)),\
            (measureHeigthBC-measureEps, measureHeigthBC+measureEps), "k", lw=lwMeasures)
    ax.annotate(r"$\Delta/2$",
                xy=(halfBetweenBCAndNP1, annotationHeigthBC), xycoords='data',
                xytext=(halfBetweenBCAndNP1, annotationHeigthBC), textcoords='data',
                size=annotateSize, va="center", ha="center",
                )

    ax.set_aspect("equal")

    # Make place
    xlim = xLen + xEps
    ylim = yLen + yEps
    ax.set_xlim((-xEps , xlim))
    ax.set_ylim((-ylim, ylim))

    fileName = "../flatGrid.{}".format(extension)
    fig.savefig(fileName, transparent=True)
    if showPlot:
        plt.show()

    return fileName

if __name__ == "__main__":
    from subprocess import Popen
    fileName = plotFlatGrid()
    # Crop with pdfCrop
    Popen("pdfcrop {0} {0}".format(fileName), shell=True).wait()
