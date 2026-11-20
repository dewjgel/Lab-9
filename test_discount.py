from supplier import Supplier
from physical_product import PhysicalProduct

from order import Order

from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


def test_discount():

    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "tech@example.com"
    )

    laptop = PhysicalProduct(
        "P001",
        "Laptop",
        120,
        10,
        2.5,
        supplier
    )

    order = Order("O001")

    order.add_order_line(laptop, 2)

    print("\nNO DISCOUNT")
    print("Total:", order.calculate_total())

    print("\nPERCENTAGE DISCOUNT")
    order.set_discount(PercentageDiscount(10))
    print("Total:", order.calculate_total())

    print("\nBULK DISCOUNT")
    order.set_discount(BulkDiscount(200, 20))
    print("Total:", order.calculate_total())

    print("\nSTUDENT DISCOUNT")
    order.set_discount(StudentDiscount())
    print("Total:", order.calculate_total())


if __name__ == "__main__":
    test_discount()
