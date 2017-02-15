#!/usr/bin/env python

import matplotlib.pyplot as plt

"""
Plots the sutainability of fusion using crude numbers.
"""

# Set rc parameters
plt.rc("axes"    , labelsize = 12)
plt.rc("xtick"   , labelsize = 12)
plt.rc("ytick"   , labelsize = 12)
plt.rc("mathtext", fontset = "cm")

def plotSustain(showPlot  = False,\
                extension ="pdf"  ):
    """
    Plots the sutainability of fusion using crude numbers from

    Melrose, J. et al 2015 - UN Nation - World population prospects
    MacKay, D. 2009 - Sustainable energy without the hot air


    Paramters
    ---------
    showPlot : bool
        Whether or not to show the plot
    extension : str
        Extension to use
    """

    daysPerYear = 365.25

    # Consumption (MacKay)
    avgConsumptionDay  = 195 # kWh/(day*person)
    avgConsumptionYear = 195*daysPerYear # kWh/(year*person)

    # Population (Melrose)
    population = 12e9

    divisor = avgConsumptionYear*population

    # Lithium ore (MacKay)
    orePopulation         = 6e9
    oreKwhPerPersonPerDay = 10
    oreYears              = 1e3
    oreDays               = oreYears*daysPerYear
    oreKWh     = oreKwhPerPersonPerDay*orePopulation*oreDays
    oreSustain = oreKWh/divisor

    # Lithium seawater (MacKay)
    seaPopulation         = 6e9
    seaKwhPerPersonPerDay = 105
    seaYears              = 1e6
    seaDays               = seaYears*daysPerYear
    seaKWh     = seaKwhPerPersonPerDay*seaPopulation*seaDays
    seaSustain = seaKWh/divisor

    # Pure Deuterium (MacKay)
    DDPopulation         = 60e9
    DDKwhPerPersonPerDay = 30e3
    DDYears              = 1e6
    DDDays               = DDYears*daysPerYear
    DDKWh = DDKwhPerPersonPerDay*DDPopulation*DDDays
    DDSustain = DDKWh/divisor

    redGiant = 5e9

    # Create the figure
    fig, ax = plt.subplots(figsize = (4,1))

    # Do the plot
    yTicks = (r"$\mathrm{\;\;Li\;from\;ore}$",\
              r"$\mathrm{\;\;Li\;from\;seawater}$",\
              r"$\mathrm{\;\;Pure\;D}$",\
              r"$\mathrm{\;\;Sun\;turns\;into\;red\;giant}$")
    sustainNumbers = (oreSustain, seaSustain, DDSustain, redGiant)
    fusionType     = tuple(range(len(sustainNumbers)))

    # Plot
    rects = ax.barh(fusionType, sustainNumbers)
    ax.invert_yaxis()

    # Do axes nice
    ax.set_xscale("log")
    ax.spines["top"]  .set_visible(False)
    ax.spines["left"] .set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_xlabel(r"$\mathrm{Years}$")

    # Set text
    for nr, (rect, txt) in enumerate(zip(rects, yTicks)):
        width  = rect.get_width()
        height = rect.get_y()
        x      = width
        y      = height + rect.get_height()/2
        ax.text(x, y, txt, ha="left", va="center")
        if nr == 3:
            rect.set_color("red")

    fileName = "../fusionSustain.{}".format(extension)
    fig.savefig(fileName, transparent=True, bbox_inches="tight")
    if showPlot:
        plt.show()

    return fileName

if __name__ == "__main__":
    from subprocess import Popen
    # Plot the odd mode
    fileName = plotSustain()
    # Crop with pdfCrop
    Popen("pdfcrop {0} {0}".format(fileName), shell=True).wait()
