import pytest
from ingredient import Ingredient
from date import *


class TestIngredient:
    def test_get_price(self):
        # Arrange
        ingredient = Ingredient(INGREDIENT_2, INGREDIENT_1, PRICE)

        # Act
        expected_price = ingredient.get_price()

        # Assert
        assert expected_price == PRICE

    def test_get_name(self):
        # Arrange
        ingredient = Ingredient(INGREDIENT_2, INGREDIENT_1, PRICE)

        # Act
        expected_name = ingredient.get_name()

        # Assert
        assert expected_name == INGREDIENT_1

    def test_get_type(self):
        # Arrange
        ingredient = Ingredient(INGREDIENT_2, INGREDIENT_1, PRICE)

        # Act
        expected_type = ingredient.get_type()

        # Assert
        assert expected_type == INGREDIENT_2
