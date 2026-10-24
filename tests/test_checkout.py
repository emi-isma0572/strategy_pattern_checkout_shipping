import pytest

from strategy_checkout.checkout import Checkout
from strategy_checkout.models import Order
from strategy_checkout.strategies import (
    ShippingCostStrategy,
    StandardShipping,
    ExpressShipping,
    PickupShipping,
    SameDayShipping,
)


def test_standard_shipping_costs_49_below_threshold():
    checkout = Checkout(StandardShipping())
    assert checkout.shipping_cost(Order(750.0, 2.0)) == 49.0


def test_standard_shipping_is_free_at_1000_or_more():
    checkout = Checkout(StandardShipping())
    assert checkout.shipping_cost(Order(1250.0, 3.5)) == 0.0


def test_express_shipping_uses_base_plus_weight():
    checkout = Checkout(ExpressShipping())
    assert checkout.shipping_cost(Order(500.0, 3.5)) == 141.0


def test_pickup_is_free():
    checkout = Checkout(PickupShipping())
    assert checkout.shipping_cost(Order(500.0, 3.5)) == 0.0


def test_total_adds_shipping_cost():
    checkout = Checkout(StandardShipping())
    assert checkout.total(Order(500.0, 2.0)) == 549.0


def test_same_day_shipping_uses_base_plus_weight():
    checkout = Checkout(SameDayShipping())
    assert checkout.shipping_cost(Order(500.0, 3.0)) == 203.0


def test_same_day_total():
    checkout = Checkout(SameDayShipping())
    assert checkout.total(Order(500.0, 3.0)) == 703.0


def test_strategies_follow_abstract_contract():
    strategies = [
        StandardShipping(),
        ExpressShipping(),
        PickupShipping(),
        SameDayShipping(),
    ]

    for strategy in strategies:
        assert isinstance(strategy, ShippingCostStrategy)


def test_abstract_strategy_cannot_be_instantiated():
    with pytest.raises(TypeError):
        ShippingCostStrategy()