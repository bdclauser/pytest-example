from pytest_bdd import scenario, given, when, then

from cucumbers import CucumberBasket


@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass


@given("the basket has 2 cucumbers")
def basket():
    return CucumberBasket(initial_count=2)


@when("4 cucumbers are added to basket")
def add_cucumbers(basket):
    basket.add(4)


@then("the basket contains 6 cucumbers")
def basket_has_total(basket):
    assert basket.count == 6
