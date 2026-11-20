from product import Product
from order_line import OrderLine

from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order:

    def __init__(
        self,
        order_id: str,
        discount: DiscountStrategy = None
    ) -> None:

        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

        self.discount = discount if discount is not None else NoDiscount()

        if not isinstance(self.discount, DiscountStrategy):
            raise TypeError("Discount must be a DiscountStrategy.")

    def set_discount(self, discount: DiscountStrategy) -> None:

        if not isinstance(discount, DiscountStrategy):
            raise TypeError("Discount must be a DiscountStrategy.")

        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:

        order_line = OrderLine(product, quantity)

        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> bool:

        if index < 0 or index >= len(self.order_lines):
            return False

        self.order_lines.pop(index)
        return True

    def calculate_total(self) -> float:

        total = sum(
            line.calculate_subtotal()
            for line in self.order_lines
        )

        return self.discount.apply(total)

    def display_order(self) -> None:

        print(f"\nOrder ID: {self.order_id}")
        print("--------------------------------")

        for order_line in self.order_lines:
            order_line.display_information()
            print()

        print("--------------------------------")
        print(f"Order Total: ${self.calculate_total():.2f}")
