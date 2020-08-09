# units types and allowed options

MEASURMENT_TYPES = ["mass", "volume", "each"]

# mass units
grams = {"display_name": "grams",
        "allowed_names": ["grams", "gram", "g", "g."],
        "amt_in_grams": 1}

pounds = {"display_name": "lbs",
        "allowed_names": ["pounds", "pound", "lb", "lbs", "lb.", "lbs."],
        "amt_in_grams": 453.592}

mass_ounce = {"display_name": "oz (mass)",
        "allowed_names": ["ounces", "ounce", "oz", "oz."],
        "amt_in_grams": 28.3495}

MASS_UNITS = [grams, pounds, mass_ounces]

# volumetric units
ml = {"display_name": "mL",
        "allowed_names": ["ml", "milliliters", "milliliter"],
        "amt_in_ml": 1}

fluid_ounce = {"display_name": "oz (fluid)",
        "allowed_names": ["ounces", "ounce", "oz", "oz."],
        "amt_in_ml": 29.5735}

liter = {"display_name": "L",
        "allowed_names": ["l", "liter", "liters"],
        "amt_in_ml": 1000}
# TODO: cups, pints, quarts, gallons, tbsp, tsp

# each units
each = {"display_name": "each",
        "allowed_names": ["each", "individual", "ea", "ea."]}
EACH_UNITS = [each]
