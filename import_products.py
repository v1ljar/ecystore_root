import csv
from EcyShop.models import Product  # Import your Product model


def create_products_from_csv():
    with open('C:/Users/vilja/OneDrive/Töölaud/EcyShop/ecystore_root/EcyShop/templates/csv_file.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = Product(
                title=row['title'],
                description=row['description'],
                origin=row['origin'],
                price=float(row['price']),
                discount_percentage=int(row['discount_percentage']),
                brand=row['brand'],
                category=row['category'],
            )
            product.save()


if __name__ == "__main__":
    create_products_from_csv()
