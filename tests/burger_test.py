import pytest
from unittest.mock import Mock
from burger import Burger
from date import *


class TestBurger:
    def test_set_buns_name(self):
        # Arrange
        burger = Burger()
        bun_mock = Mock()

        # Act
        burger.set_buns(bun_mock)

        # Assert
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        # Arrange
        burger = Burger()
        ingredient = Mock()

        # Act
        burger.add_ingredient(ingredient)

        # Assert
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        # Arrange
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)

        # Act
        burger.remove_ingredient(0)

        # Assert
        assert burger.ingredients == []

    def test_move_ingredient(self):
        # Arrange
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_1.name = INGREDIENT_1
        ingredient_2.name = INGREDIENT_2
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        # Act
        burger.move_ingredient(0, 1)

        # Assert
        assert burger.ingredients[0].name == INGREDIENT_2
        assert burger.ingredients[1].name == INGREDIENT_1

    def test_get_price(self):
        # Arrange
        burger = Burger()

        bun_mock = Mock()
        bun_mock.get_price.return_value = 5

        ingredient_1_mock = Mock()
        ingredient_1_mock.get_price.return_value = 10

        ingredient_2_mock = Mock()
        ingredient_2_mock.get_price.return_value = 7

        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_1_mock)
        burger.add_ingredient(ingredient_2_mock)

        # Act
        price = burger.get_price()

        # Assert
        assert price == 27

    def test_get_receipt(self):
        # Arrange
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = INGREDIENT_1

        ingredient_1_mock = Mock()
        ingredient_1_mock.get_name.return_value = INGREDIENT_2
        ingredient_1_mock.get_type.return_value = INGREDIENT_3

        bun_mock.get_price.return_value = 5
        ingredient_1_mock.get_price.return_value = 10

        # Act
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_1_mock)

        # Assert
        assert burger.get_receipt() == RECEIPT
