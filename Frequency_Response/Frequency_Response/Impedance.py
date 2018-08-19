# The aim of this module is to develop a generic data structure to represent the complex impedance of 
# the three main lumped circuit elements: Resistor, Capacitor, Inductor
# The plan is to have a base class with the three elements defined as derived classes
# R. Sheehan 17 - 8 - 2018

# import pre-requisite modules
import math
import scipy
import numpy as np
import matplotlib.pyplot as plt
import Common

MOD_NAME_STR = "Impedance" # use this in exception handling messages

# define a constant value

class impedance(object):

    # base class for derived objects resistor, capacitor, inductor
    # base class has private members
    # __vscale, __fscale, __frequency, __omega
    # object is instantiated with default values

    def __init__(self): 
        self.FUNC_NAME = ".impedance(object)" # use this in exception handling messages
        
        self.ERR_STATEMENT = "Error: " + MOD_NAME_STR + self.FUNC_NAME
        
        self.set_vscale(Common.SI_Prefices["one"])

        self.set_fscale(Common.SI_Prefices["one"])
        
        self.set_f(1.0, Common.SI_Prefices["one"])
            
    # public getters
    def get_vscale(self):
        return self.__vscale # return value of private member __vscale

    def get_fscale(self):
        return self.__fscale # return value of private member __fscale

    def get_f(self):
        return self.__frequency # return value of private member __frequency

    def get_w(self):
        return self.__omega # return value of private member __omega

    # public setters
    def set_vscale(self, value):
        try:
            if Common.dict_contains_value(Common.SI_Prefices, value):
                self.__vscale = value
            else:
                self.__vscale = 1.0
                raise Exception
        except Exception:
            print(self.ERR_STATEMENT)

    def set_fscale(self, value):
        try:
            if Common.dict_contains_value(Common.SI_Prefices, value):
                self.__fscale = value
            else:
                self.__fscale = 1.0
                raise Exception
        except Exception:
            print(self.ERR_STATEMENT)

    def set_f(self, value, scale):
        try:
            self.set_fscale(scale)
            if value >= 0.0:
                self.__frequency = value * self.__fscale # define f val at the appropriate scale
                self.__omega = Common.TWO_PI * self.__frequency # angular frequency
            else:
                self.__frequency = 0.0
                self.__omega = 0.0
                raise Exception
        except Exception:
            print(self.ERR_STATEMENT)

class resistor(impedance):

    # class for defining a resistor object
    # resistor is derived from base class impedance
    # resistor contains private member __resistance

    def __init__(self, rval, vscl):
        self.FUNC_NAME = ".resistor(impedance)" # use this in exception handling messages
        
        self.ERR_STATEMENT = "Error: " + MOD_NAME_STR + self.FUNC_NAME
        
        impedance.__init__(self)
        
        self.set_R(rval, vscl)

    # public getter
    def get_R(self):
        return self.__resistance

    # public setter
    def set_R(self, value, vscl):
        try:
            self.set_vscale(vscl)
            if value >= 0.0:
                self.__resistance = value * self.get_vscale()            
            else:
                self.__resistance = 0.0
                raise Exception
        except Exception:
            print(self.ERR_STATEMENT)

class capacitor(impedance):

    # class for defining a capacitor object
    # capacitor is derived from base class impedance
    # capacitor contains private member __capacitance

    def __init__(self, cval, vscl, fval, fscl):
        self.FUNC_NAME = ".capacitor(impedance)" # use this in exception handling messages
        
        self.ERR_STATEMENT = "Error: " + MOD_NAME_STR + self.FUNC_NAME  
        
        impedance.__init__(self)
        
        self.set_C(cval, vscl, fval, fscl)

    # public getter
    def get_C(self):
        return self.__capacitance

    # public setter
    def set_C(self, value, vscl, freq, fscl):
        try:
            self.set_vscale(vscl)
            self.set_f(freq, fscl)
            if value >= 0.0 and self.get_w() > 0.0:
                denom = complex(0.0, self.get_w() * value * self.get_vscale())
                self.__capacitance = 1.0 / denom
            else:
                self.__capacitance = complex(0.0, 0.0)
                raise Exception
        except Exception:
            print(self.ERR_STATEMENT)

class inductor(impedance):

    # class for defining an inductor object
    # inductor is derived from base class impedance
    # inductor contains private member __inductance

    def __init__(self, cval, vscl, fval, fscl):
        self.FUNC_NAME = ".inductor(impedance)" # use this in exception handling messages
        
        self.ERR_STATEMENT = "Error: " + MOD_NAME_STR + self.FUNC_NAME  
        
        impedance.__init__(self)
        
        self.set_L(cval, vscl, fval, fscl)

    # public getter
    def get_L(self):
        return self.__inductance

    # public setter
    def set_L(self, value, vscl, freq, fscl):
        try:
            self.set_vscale(vscl)
            self.set_f(freq, fscl)
            if value >= 0.0 and self.get_w() > 0.0:                
                self.__inductance = complex(0.0, self.get_w() * value * self.get_vscale())
            else:
                self.__inductance = complex(0.0, 0.0)
                raise Exception
        except Exception:
            print(self.ERR_STATEMENT)