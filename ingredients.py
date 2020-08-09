"""
Module for ingredients

"""

class Quantity():

    def __init__(self, unit, amount, meas_type="mass"):
        """
        Initialize quantity

        Input:
            unit - unit of measure (cups, grams, etc)
            amount - amount of given unit
            meas_type - flag indicating what type of measurement:
                either "mass" or "volume"
        """

        self.__amount__ = amount
        self.__unit__ = unit
        self.__meastype__ = meas_type

    def set_amount(self, amt):
        self.__amount__ = amt

    def get_amount(self):
        return self.__amount__

    def set_unit(self, unit):
        self.__amount__ = convert_unit(self.__amount__, self.__unit__, unit)
        self.__unit__ = unit

    def get_unit(self):
        return self.__unit__

    def set_meas_type(self, meas_type):
        if self.__meastype__ != meas_type:
            print("Warning! Measurement type is changing!")
            self.__meastype__ = meas_type



class Ingredient():

    def __init__(self, name, classification, quantity):
        """
        Initialize ingredient

        Input:
            name - name of item (human readable)
            classification - what kind of food is it: dairy, meat, etc
            quantity - object of type Quantity
        """

        self.__name__ = name
        self.__class__ = classification
        self.__quant__ = quantity

    def set_class(self, classification):
        self.__class__ = classification

    def get_class(self):
        return self.__class__

    def set_name(self, name):
        self.__name__ = name

    def get_name(self):
        return self.__name__

    def set_quantity(self, quant):
        self.__quant__ = quat

    def get_quantity(self):
        return self.__quant__
        
