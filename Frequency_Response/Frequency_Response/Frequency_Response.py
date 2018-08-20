# Import libraries
# You should try an import the bare minimum of modules
import sys # access system routines
import os
import glob
import re

import math
import scipy
import numpy
import matplotlib.pyplot as plt

# add path to our file
sys.path.append('c:/Users/Robert/Programming/Python/Common/')
sys.path.append('c:/Users/Robert/Programming/Python/Plotting/')

import Common
import Plotting
import Impedance
import Circuit_Models

def main():
    pass

if __name__ == '__main__':
    main()

    pwd = os.getcwd() # get current working directory

    print(pwd)

    Z = Impedance.impedance()

    print(Z.get_vscale())
    
    print(Z.get_f())
    
    print(Z.get_vscale())
    
    print(Z.get_w())

    print()
    
    Z.set_f(4, Common.SI_Prefices["Giga"])

    Z.set_vscale(Common.SI_Prefices["pico"])

    print(Z.get_f())

    print(Z.get_vscale())

    print(Z.get_w())

    print()

    R = Impedance.resistor(10, Common.SI_Prefices["kilo"])

    print(R.get_R())
    print(R.get_vscale())
    print(R.get_R()/R.get_vscale())
    
    print()

    C = Impedance.capacitor(470, Common.SI_Prefices["pico"], 62, Common.SI_Prefices["Mega"])

    print(C.get_C()/C.get_vscale())
    print(C.get_ZC())

    print()

    L = Impedance.inductor(90, Common.SI_Prefices["nano"], 62, Common.SI_Prefices["Mega"])

    print(L.get_L()/L.get_vscale())
    print(L.get_ZL())

    print()

    rval = 50; rscl = Common.SI_Prefices["one"]
    cval = 4700; cscl = Common.SI_Prefices["pico"]
    
    f = 60; fscl = Common.SI_Prefices["kilo"]

    RC = Circuit_Models.RC_voltage_divider(rval, rscl, cval, cscl, f, fscl)

    print(f*fscl, RC)
    
    f = 60; fscl = Common.SI_Prefices["Mega"]

    RC = Circuit_Models.RC_voltage_divider(rval, rscl, cval, cscl, f, fscl)

    print(f*fscl, RC)

    f = 60; fscl = Common.SI_Prefices["Giga"]

    RC = Circuit_Models.RC_voltage_divider(rval, rscl, cval, cscl, f, fscl)

    print(f*fscl, RC)

    print()

    print(Common.convert_deg_rad(90)/math.pi)

    print(Common.convert_rad_deg(math.pi/4.0))