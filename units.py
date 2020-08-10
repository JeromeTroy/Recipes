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
each = {"display_name": "each",
        "allowed_names": ["each", "individual", "ea", "ea."],
        "amount_in_each": 1,
        "unit_type": "individual"}
EACH_UNITS = [each]
