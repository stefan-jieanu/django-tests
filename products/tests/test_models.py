from django.core.exceptions import ValidationError
from django.test import TestCase

from products.models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product(name="Mouse", price=100, stock_count=13)

    def test_total_value(self):
        self.assertTrue(self.product.total_value() == 1300)

    def test_discount(self):
        self.assertTrue(self.product.get_discounted_price(10), 90)
        # self.assertEqual()

    def test_negative_price(self):
        self.product.price = -1

        with self.assertRaises(ValidationError):
            self.product.clean()