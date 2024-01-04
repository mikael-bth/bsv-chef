import pytest

from src.controllers.recipecontroller import RecipeController
from src.util.dao import DAO

# Creating DAO with new collection for testing
testDAO = DAO("test")
testDAO.create({
    "name": "Salt",
    "quantity": 275,
    "unit": "gram"})
testDAO.create({
    "name": "Sugar",
    "quantity": 300,
    "unit": "gram"})
testDAO.create({
    "name": "Flour",
    "quantity": 450,
    "unit": "gram"})

controller = RecipeController(testDAO)

# add your test case implementation here
@pytest.mark.unit
def test_get_all():
    """
    Test that get_all doesnt raise an exception
    """
    try:
        controller.get_available_items()
    except Exception:
        assert False

@pytest.mark.unit
def test_minimum_quantity_0():
    """
    Test that get_available_items returns the right item with minimum_quantity 0
    """
    items = controller.get_available_items(0)

    assert items == {{
    "name": "Salt",
    "quantity": 275,
    "unit": "gram"}, {
    "name": "Sugar",
    "quantity": 300,
    "unit": "gram"}, {
    "name": "Flour",
    "quantity": 450,
    "unit": "gram"}}


# Drops the collection when tests are done
testDAO.drop()