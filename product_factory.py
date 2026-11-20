from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        **kwargs
    ) -> Product:

        product_type = product_type.lower()

        if product_type == "physical":

            if "weight" not in kwargs:
                raise ValueError("Physical product requires a weight.")

            return PhysicalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                kwargs["weight"],
                supplier
            )

        elif product_type == "digital":

            if "download_size" not in kwargs:
                raise ValueError("Digital product requires a download size.")

            return DigitalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                kwargs["download_size"],
                supplier
            )

        else:

            raise ValueError(f"Unknown product type: {product_type}")
