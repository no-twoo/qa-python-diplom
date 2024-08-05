import pytest
from bun import Bun
from date import *


class TestBun:
    def test_get_name(self):
        # Arrange
        bun = Bun(INGREDIENT_1, PRICE)

        # Act
        expected_name = bun.get_name()

        # Assert
        assert expected_name == INGREDIENT_1

    def test_get_price(self):
        # Arrange
        bun = Bun(INGREDIENT_1, PRICE)

        # Act
        expected_price = bun.get_price()

        # Assert
        assert expected_price == PRICE
