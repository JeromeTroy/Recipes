from units import *
from ingredients import *

class ShoppingList(list):

    def __init__(self):
        self.__ingredient_list__ = []

    def build_shopping_list(self, string_list):
        shopping_list = ShoppingList()
        for item in string_list:
            ingredient = parse_line(item)
            shopping_list.add(ingredient)

        return shopping_list

    def get_list(self):
        return self.__ingredient_list__[:]

    def add(self, ingredient):

        lst = self.get_list()
        new_item = None
        index = None

        for i in range(len(self.get_list())):

            try:
                new_item = lst[i] + ingredient
                index = i
            except MeasurementTypeMismatch:
                pass
            except IngredientMismatch:
                pass

        if new_item is None:
            self.__ingredient_list__.append(ingredient)
        else:
            self.__ingredient_list__[index] = new_item


    def __str__(self):

        string = ""
        for ingredient in self.__ingredient_list__:
            string += str(ingredient)
            string += "\n"
        return string

if __name__ == "__main__":
    print("Executing Tests")

    ingredient_list = [
        "4 pounds of carrots (produce)",
        "2 potatoes (produce)",
        "16 apples (produce)",
        "400 grams shredded carrots (produce)",
        "5 slices of bread (bread)",
        "1 loaf of bread (bread)"
    ]

    grocery_list = ShoppingList().build_shopping_list(ingredient_list)
    print(grocery_list)
