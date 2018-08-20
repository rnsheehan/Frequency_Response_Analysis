# Python module for implementing various circuit models
# The aim is to develop code that can fit RC circuit models to measured response data
# Include a plotting method
# R. Sheehan 20 - 8 - 2018

# import pre-requisite modules
import math
import scipy
import numpy as np
import matplotlib.pyplot as plt
import Common
import Impedance
import cmath # required module for complex number manipulation

MOD_NAME_STR = "Circuit_Models" # use this in exception handling messages

def RC_voltage_divider(rval, rscl, cval, cscl, fval, fscl):
    # simple RC based voltage divider
    # rval is the resistance value, rscl is its associated scale
    # cval is the capacitance value, cscl is its associated scale
    # f is the frequency at which the response is calculated, fscl is its associated scale

    FUNC_NAME = ".RC_voltage_divider()" # use this in exception handling messages        
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME

    try:
        c1 = True if rval > 0.0 else False
        c2 = Common.dict_contains_value(Common.SI_Prefices, rscl)
        c3 = True if cval > 0.0 else False
        c4 = Common.dict_contains_value(Common.SI_Prefices, cscl)
        c5 = True if fval > 0.0 else False
        c6 = Common.dict_contains_value(Common.SI_Prefices, fscl)
        c7 = True if c1 and c2 and c3 and c4 and c5 and c6 else False

        if c7:
            R = Impedance.resistor(rval, rscl)

            C = Impedance.capacitor(cval, cscl, fval, fscl)

            term = complex(0.0, C.get_w() * C.get_C() * R.get_R() )

            denom = cmath.sqrt( 1.0 + term )

            resp = 1.0 / denom

            mag_resp = abs(resp)

            phase_resp = cmath.phase(resp)

            return [mag_resp, phase_resp]
        else:
            raise Exception
    except Exception:
        print(ERR_STATEMENT)