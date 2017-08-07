# Global numerical modeling of magnetized plasma in a linear device

Submitted to the Technical University of Denmark on March 6th 2017.

Defended in Kongens Lyngby on May 19th 2017.

## Abstract

Understanding the turbulent transport in the plasma-edge in fusion devices is of utmost importance in order to make precise predictions for future fusion devices.
The plasma turbulence observed in linear devices shares many important features with the turbulence observed in the edge of fusion devices, and are easier to diagnose due to lower temperatures and a better access to the plasma.
In order to gain greater insight into this complex turbulent behavior, numerical simulations of plasma in a linear device are performed in this thesis.

Here, a three-dimensional drift-fluid model is derived from first principles for a magnetized plasma in a linear device.
To account for the fluctuations at the same level as the background plasma, the traditional split between background and fluctuations has not been made.
The model is implemented using the BOUT++ framework and is solved numerically.
Special attention is given to the treatment of the singularity at the cylinder axis, and at the inversion of the non-linear elliptic equation, which is done to obtain the electrical potential.
The evolution of the plasma through the steady-state, linear phase, and turbulent phase is investigated and compared for different B-field strengths.
It is found that drift-waves are responsible for the onset of turbulence, and that the turbulent radial flux is causing a flattening of the density profiles.
Coherent structures from the intermittent radial flux in the turbulent state are investigated.

Results of simulations using the Boussinesq approximation is compared to full simulations.
It is found that the Boussinesq approximation leads to an unphysical increase of the electrical potential as ions and electrons are lost at a different rate.

Finally, the results from the full simulations are compared with simulations performed at different ionization levels, using a simple model for plasma interaction with neutrals.
It is found that the steady state and the saturated state of the system bifurcates when the neutral interaction dominates the electron-ion collisions

## Keywords:

Cylindrical plasma, Drift-fluid equations, Numerical modeling, Drift-waves, Plasma turbulence, Coherent structures, Sheath boundary condition

## Notes
The `master` branch contains the latest corrections.

Run the `Makefile` to build the `pdf`, or see [releases](https://github.com/CELMA-project/dissertation/releases) for already built versions of the thesis.
