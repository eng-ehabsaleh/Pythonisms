import pytest
from pythonisms.iter import LinkedList
from pythonisms import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_for_in():

    foods = LinkedList(("Rice", "tomato", "fries"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert foods_list == ["Rice", "tomato", "fries"]


def test_list_comprehension():

    foods = LinkedList(("Rice", "tomato", "fries"))

    cap_foods = [food.upper() for food in foods]

    assert cap_foods == ["RICE", "TOMATO", "FRIES"]


def test_list_cast():

    food_list = ["Rice", "tomato", "fries"]

    foods = LinkedList(food_list)

    assert list(foods) == food_list


def test_range():

    num_range = range(1, 20+1)

    nums = LinkedList(num_range)

    assert len(nums) == 20


def test_filter():

    nums = LinkedList(range(1, 21))

    odds = [num for num in nums if num % 2]

    assert odds == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def test_next():

    foods = LinkedList(["Rice", "Tomato"])

    iterator = iter(foods)

    assert next(iterator) == "Rice"
    assert next(iterator) == "Tomato"
    


def test_stop_iteration():

    foods = LinkedList(["Rice", "Tomato", "Fries"])

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)


def test_str():
    foods = LinkedList(["Rice", "Tomato", "Fries"])
    assert str(foods) == "[ Rice ] ==> [ Tomato ] ==> [ Fries ] ==> None"

# dunder method tests


def test_equals():

    lla = LinkedList(["Rice", "Tomato", "Fries"])
    llb = LinkedList(["Rice", "Tomato", "Fries"])

    assert lla == llb


def test_get_item():

    foods = LinkedList(["Rice", "Tomato", "Fries"])

    assert foods[0] == "Rice"


def test_get_item_out_of_range():

    foods = LinkedList(["Rice", "Tomato", "Fries"])

    with pytest.raises(IndexError):
        foods[100]
