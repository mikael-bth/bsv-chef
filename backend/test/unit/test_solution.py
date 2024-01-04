import pytest
import unittest.mock as mock

from src.controllers.recipecontroller import RecipeController

items = [{"name": "Salt",
    "quantity": 275,
    "unit": "gram"}, {
    "name": "Sugar",
    "quantity": 300,
    "unit": "gram"}, {
    "name": "Flour",
    "quantity": 450,
    "unit": "gram"}]

@pytest.fixture
def sut():
    mockedDAO = mock.MagicMock()
    mockedDAO.find.return_value = items
    mockedsut = RecipeController(mockedDAO)
    return mockedsut

# add your test case implementation here
@pytest.mark.unit
def test_get_all(sut):
    """
    Test that get_all doesnt raise an exception
    """
    try:
        sut.get_available_items()
    except Exception:
        assert False

@pytest.mark.unit
def test_minimum_quantity_0(sut):
    """
    Test that get_available_items returns the right item with minimum_quantity 0
    """
    result = sut.get_available_items(0)

    assert result == {"Salt": 275, "Sugar": 300, "Flour": 450}

@pytest.mark.unit
def test_minimum_quantity_280(sut):
    """
    Test that get_available_items returns the right item with minimum_quantity 300
    """
    result = sut.get_available_items(280)

    assert result == {"Sugar": 300, "Flour": 450}
@pytest.mark.unit
def test_minimum_quantity_400(sut):
    """
    Test that get_available_items returns the right item with minimum_quantity 300
    """
    result = sut.get_available_items(400)

    assert result == {"Flour": 450}

@pytest.mark.unit
def test_minimum_quantity_400(sut):
    """
    Test that get_available_items returns the right item with minimum_quantity 300
    """
    result = sut.get_available_items(500)

    assert result == {}