from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def finding_obj_name(self, p_n, list_with_products):
        try:
            return next(filter(lambda x: x.name == p_n, list_with_products))
        except StopIteration:
            return None

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return self.finding_obj_name(product_name, self.products)

    def remove(self, product_name):
        searched_product = self.finding_obj_name(product_name, self.products)
        if searched_product:
            self.products.remove(searched_product)

    def __repr__(self):
        result = '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
        return result

