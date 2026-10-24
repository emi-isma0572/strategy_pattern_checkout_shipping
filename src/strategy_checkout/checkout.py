
from .models import Order
from .strategies import ShippingCostStrategy


class Checkout:
    """Calculates order totals using an injected shipping strategy."""

    def __init__(self, shipping_strategy: ShippingCostStrategy):
        self._shipping_strategy = shipping_strategy

    def shipping_cost(self, order: Order) -> float:
        return self._shipping_strategy.calculate(order)

    def total(self, order: Order) -> float:
        return order.subtotal + self.shipping_cost(order)
