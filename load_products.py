import csv

from product_factory import ProductFactory
from inventory import Inventory
from supplier import Supplier


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded = 0

    try:

        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:

        print(f"Products file not found: {path}")

    else:

        with file:

            reader = csv.reader(file)

            next(reader, None)  # Skip header

            for row in reader:

                try:

                    product_type = row[0].strip()
                    product_id = row[1].strip()
                    name = row[2].strip()
                    price = float(row[3])
                    stock_quantity = int(row[4])

                    # Create product through Factory
                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        price,
                        stock_quantity,
                        supplier,
                        weight=1.5,
                        download_size=500
                    )

                    inventory.add_product(product)

                    loaded += 1

                except ValueError as error:

                    print(f"Skipping invalid row {row}: {error}")

                except IndexError:

                    print(f"Skipping incomplete row: {row}")

        print(f"{loaded} products loaded.")

    finally:

        print("Load attempt finished.")
