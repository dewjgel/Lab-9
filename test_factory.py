from supplier import Supplier
from product_factory import ProductFactory


def test_factory():

    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "tech@example.com"
    )

    physical = ProductFactory.create(
        "physical",
        "P001",
        "Laptop",
        1200,
        15,
        supplier,
        weight=2.5
    )

    digital = ProductFactory.create(
        "digital",
        "D001",
        "Antivirus",
        45,
        25,
        supplier,
        download_size=500
    )

    physical.display_information()
    digital.display_information()

    try:

        ProductFactory.create(
            "service",
            "S001",
            "Installation",
            30,
            5,
            supplier
        )

    except ValueError as error:

        print("Factory error:", error)


if __name__ == "__main__":
    test_factory()
