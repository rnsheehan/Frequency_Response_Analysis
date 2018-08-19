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

    print(C.get_C())

    L = Impedance.inductor(90, Common.SI_Prefices["nano"], 62, Common.SI_Prefices["Mega"])

    print(L.get_L())

    