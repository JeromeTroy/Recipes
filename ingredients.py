"""
Module for ingredients

"""
from units import *

class Quantity():

    def __init__(self, unit, amount):
        """
        Initialize quantity

        Input:
            unit - unit of measure (cups, grams, etc)
            amount - amount of given unit
        """

        self.__amount__ = amount
        self.__unit__ = unit

    def __str__(self):
        """
        Helper for printing
        """
        string = "{:.2f} {:s}".format(self.get_amount(), self.get_unit()["display_name"])
        return string

    def __add__(self, quantity):
        if self.get_meas_type() != quantity.get_meas_type():
            # measurement types do not match
            raise MeasurementTypeMismatch()

        else:
            if self.get_unit() != quantity.get_unit():

                # decide perfered unit and convert everything
                perfered_unit = self.get_unit()
                if self.get_meas_type() == "mass":
                    base_unit = "amt_in_grams"
                elif self.get_meas_type() == "volume":
                    base_unit = "amt_in_ml"
                else:
                    base_unit = "amount_in_each"

                if quantity.get_unit()[base_unit] > perfered_unit[base_unit]:
                    perfered_unit = quantity.get_unit()
                    self.convert(perfered_unit)
                else:
                    quantity.convert(perfered_unit)
                
                result = Quantity(self.get_unit(),
                        self.get_amount() + quantity.get_amount())
                return result
            else:
                result = Quantity(self.get_unit(),
                        self.get_amount() + quantity.get_amount())
                return result

    def set_amount(self, amt):
        self.__amount__ = amt

    def get_amount(self):
        return self.__amount__

    def set_unit(self, unit):
        self.__unit__ = unit

    def get_unit(self):
        return self.__unit__
    
    def get_meas_type(self):
        return self.get_unit()["unit_type"]

    def convert(self, new_unit):
        """
        Convert quantity from current unit to a new unit of measure

        Input: 
            new_unit - new unit of measure
        """

        if new_unit["unit_type"] == self.get_meas_type():

            if new_unit["unit_type"] == "mass":
                base_unit = "amt_in_grams"
            elif new_unit["unit_type"] == "volume":
                base_unit = "amt_in_ml"

            current_unit = self.get_unit()
            
            conversion_factor = current_unit[base_unit] / new_unit[base_unit]
            new_amt = self.get_amount() * conversion_factor

            self.set_unit(new_unit)
            self.set_amount(new_amt)

        else:
            raise MeasurementTypeMismatch()






class Ingredient():

    def __init__(self, name, category, quantity):
        """
        Initialize ingredient

        Input:
            name - name of item (human readable)
            category - what kind of food is it: dairy, meat, etc
            quantity - object of type Quantity
        """

        self.__name__ = name.lower()
        self.__category__ = category.lower()
        self.__quant__ = quantity

    def set_category(self, category):
        self.__category__ = category

    def get_category(self):
        return self.__category__

    def set_name(self, name):
        self.__name__ = name

    def get_name(self):
        return self.__name__

    def set_quantity(self, quant):
        self.__quant__ = quant

    def get_quantity(self):
        return self.__quant__

    def __add__(self, other_ingredient):
        same_category = self.get_category() == other_ingredient.get_category()
        same_name = self.get_name() == other_ingredient.get_name()

        if same_category and same_name:
            quantity = self.get_quantity() + other_ingredient.get_quantity()
            result = Ingredient(self.get_name(), self.get_category(), quantity)
            return result

        else:
            raise IngredientMismatch
    
    def __str__(self):
        """
        Printing helper
        """
        string = str(self.get_quantity())
        string += " of {:s} ({:s})".format(self.get_name(), self.get_category())
        return string

class MeasurementTypeMismatch(Exception):

    def __init__(self, message="Quantity measurement types do not match"):
        self.message = message

class IngredientMismatch(Exception):
    
    def __init__(self, message="Ingredient types do not match"):
        self.message = message
