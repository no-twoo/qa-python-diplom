import pytest

from typing import List
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()

        expected_result: List[Bun] = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300),
        ]

        assert len(expected_result) == len(database.available_buns())
        for i, bun in enumerate(database.available_buns()):
            assert bun.get_price() == expected_result[i].get_price()
            assert bun.get_name() == expected_result[i].get_name()

    def test_available_ingredients(self):
        database = Database()
        expected_result: List[Ingredient] = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        assert len(expected_result) == len(database.available_ingredients())
        for i, ingredient in enumerate(database.available_ingredients()):
            assert ingredient.get_price() == expected_result[i].get_price()
            assert ingredient.get_name() == expected_result[i].get_name()
        