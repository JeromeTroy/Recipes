# units types and allowed options

MEASURMENT_TYPES = ["mass", "volume", "each"]

# mass units
gram = {"display_name": "grams",
        "allowed_names": ["grams", "gram", "g", "g."],
        "amt_in_grams": 1,
        "unit_type": "mass"}

pound = {"display_name": "lbs",
        "allowed_names": ["pounds", "pound", "lb", "lbs", "lb.", "lbs."],
        "amt_in_grams": 453.592,
        "unit_type": "mass"}

mass_ounce = {"display_name": "oz (mass)",
        "allowed_names": ["ounces", "ounce", "oz", "oz."],
        "amt_in_grams": 28.3495,
        "unit_type": "mass"}

MASS_UNITS = [gram, pound, mass_ounce]

# volumetric units
ml = {"display_name": "mL",
        "allowed_names": ["ml", "milliliters", "milliliter"],
        "amt_in_ml": 1,
        "unit_type": "volume"}

fluid_ounce = {"display_name": "oz (fluid)",
        "allowed_names": ["ounces", "ounce", "oz", "oz."],
        "amt_in_ml": 29.5735,
        "unit_type": "volume"}

liter = {"display_name": "L",
        "allowed_names": ["l", "liter", "liters"],
        "amt_in_ml": 1000,
        "unit_type": "volume"}

cup = {"display_name": "cups",
        "allowed_names": ["c", "cup", "cups"],
        "amt_in_ml": 236.588,
        "unit_type": "volume"}

pint = {"display_name": "pints",
        "allowed_names": ["p", "pt", "pts", "pint", "pints"],
        "amt_in_ml": 568.261,
        "unit_type": "volume"}

quart = {"display_name": "quarts",
        "allowed_names": ["qt", "qts", "quart", "quarts"],
        "amt_in_ml": 1136.5225,
        "unit_type": "volume"}

gallon = {"display_name": "gallons",
        "allowed_names": ["g", "gal", "gals", "gallon", "gallons"],
        "amt_in_ml": 4546.09,
        "unit_type": "volume"}

tablespoon = {"display_name": "tbsp",
        "allowed_names": ["tbsp", "tablespoon", "tablespoons"],
        "amt_in_ml": 14.8,
        "unit_type": "volume"}

teaspoon = {"display_name": "tsp",
        "allowed_names": ["tsp", "teaspoon", "teaspoons"],
        "amt_in_ml": 5,
        "unit_type": "volume"}

VOLUME_UNITS = [ml, fluid_ounce, liter, cup, pint, quart, gallon,
                tablespoon, teaspoon]

# each units
each = {"display_name": "",
        "allowed_names": ["each", "individual", "ea", "ea."],
        "amt_in_each": 1,
        "unit_type": "individual"}

slice = {"display_name": "slice",
        "allowed_names": ["slice", "slices"],
        "amt_in_each": 1,
        "unit_type": "individual"}

loaf = {"display_name": "loaf",
        "allowed_names": ["loaf", "loaves", "loafs"],
        "amt_in_each": 16,
        "unit_type": "individual"}

EACH_UNITS = [each, slice, loaf]

# allowed categories
CATEGORIES = ["produce", "canned", "meat", "frozen",
                "dairy", "eggs", "household", "grain",
                "snack", "beverage", "condiment",
                "baking", "coffee", "alcohol",
                "misc"]

POSSIBLE_UNIT_NAMES = []
MASS_UNIT_NAMES = []
VOLUME_UNIT_NAMES = []
EACH_UNIT_NAMES = []

for mass_unit in MASS_UNITS:
        MASS_UNIT_NAMES += mass_unit["allowed_names"]

for volume_unit in VOLUME_UNITS:
        VOLUME_UNIT_NAMES += volume_unit["allowed_names"]

for each_unit in EACH_UNITS:
        EACH_UNIT_NAMES += each_unit["allowed_names"]

POSSIBLE_UNIT_NAMES += MASS_UNIT_NAMES + VOLUME_UNIT_NAMES + EACH_UNIT_NAMES


def find_appropriate_unit(string):
        """
        Find the appropriate unit given a string

        Input:
                string - one of allowed_names
        Output:
                unit - appropriate unit
        """

        unit_list = []
        if string in MASS_UNIT_NAMES:
                unit_list = MASS_UNITS
        elif string in VOLUME_UNIT_NAMES:
                unit_list = VOLUME_UNITS
        elif string in EACH_UNIT_NAMES:
                unit_list = EACH_UNITS

        true_unit = None
        for unit in unit_list:
                if string in unit["allowed_names"]:
                        true_unit = unit
                        break
        if true_unit is not None:
                return true_unit
        else:
                raise NameError("Unit name not found!")
