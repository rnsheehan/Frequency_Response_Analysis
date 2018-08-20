# Module for testing code that is being developed
# R. Sheehan 20 - 8 - 2018

# import pre-requisite modules
import math
import scipy
import numpy as np
import matplotlib.pyplot as plt
import Common
import Impedance
import Circuit_Models
import cmath # required module for complex number manipulation

MOD_NAME_STR = "Testing" # use this in exception handling messages

def test_impedance_objects():
    # check that the operation of the impedance objects is correct
    # R. Sheehan 17 - 8 - 2018

    FUNC_NAME = ".test_impedance_objects()" # use this in exception handling messages        
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME

    try:
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
    except Exception:
        print(ERR_STATEMENT)

def test_RC_Circuit():
    # test the implementation of the formula for computing RC circuit response
    # R. Sheehan 20 - 8 - 2018

    FUNC_NAME = ".test_RC_Circuit()" # use this in exception handling messages        
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME

    try:
        rval = 1; rscl = Common.SI_Prefices["one"]
        cval = 470; cscl = Common.SI_Prefices["pico"]

        BW = Circuit_Models.RC_BW(rval, rscl, cval, cscl)

        print()
        print("3dB BW for circuit is",BW/Common.SI_Prefices["Mega"],"MHz")
        print()
    
        f = 60; fscl = Common.SI_Prefices["kilo"]

        RC = Circuit_Models.RC_voltage_divider(rval, rscl, cval, cscl, f, fscl)

        print(f*fscl, RC)
    
        f = 60; fscl = Common.SI_Prefices["Mega"]

        RC = Circuit_Models.RC_voltage_divider(rval, rscl, cval, cscl, f, fscl)

        print(f*fscl, RC)

        f = 60; fscl = Common.SI_Prefices["Giga"]

        RC = Circuit_Models.RC_voltage_divider(rval, rscl, cval, cscl, f, fscl)

        print(f*fscl, RC)
    except Exception:
        print(ERR_STATEMENT)