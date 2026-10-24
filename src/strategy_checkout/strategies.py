
from abc import ABC, abstractmethod

from .models import Order


class ShippingCostStrategy(ABC):
    """Define the contract for shipping cost strategies."""

    @abstractmethod
    def calculate(self, order: Order) -> float:
        """Calculate the shipping cost for an order."""
        pass


class StandardShipping(ShippingCostStrategy):
    """Standard shipping: free for subtotals of 1000 or more."""

    def calculate(self, order: Order) -> float:
        if order.subtotal >= 1000:
            return 0.0

        return 49.0


class ExpressShipping(ShippingCostStrategy):
    """Express shipping: 99 plus 12 per kilogram."""

    def calculate(self, order: Order) -> float:
        return 99.0 + 12.0 * order.weight_kg


class PickupShipping(ShippingCostStrategy):
    """Pickup shipping is free."""

    def calculate(self, order: Order) -> float:
        return 0.0


class SameDayShipping(ShippingCostStrategy):
    """Same Day shipping: 149 plus 18 per kilogram."""

    def calculate(self, order: Order) -> float:
        return 149.0 + 18.0 * order.weight_kg
