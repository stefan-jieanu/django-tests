from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from products.models import Product


# Create your tests here.
class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product(name='Mouse', price=100, stock_count=13)

    def test_total_value(self):
        self.assertTrue(self.product.total_value() == 1300)

    def test_discount(self):
        self.assertTrue(self.product.get_discounted_price(10), 90)
        # self.assertEqual()

    def test_negative_price(self):
        self.product.price = -1

        with self.assertRaises(ValidationError):
            self.product.clean()

# Nu creeaza o baza de date
class TestHomePage(SimpleTestCase):
    def test_homepage_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_message(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello!')


class TestProductsPage(TestCase):
    def setUp(self):
        Product.objects.create(name='Mouse', price=100, stock_count=13)
        Product.objects.create(name='MousePad', price=100, stock_count=13)

    def test_products_context(self):
        response = self.client.get(reverse('products'))
        self.assertEquals(len(response.context['products']), 2)
        self.assertContains(response, 'Mouse')
        self.assertContains(response, 'MousePad')
        self.assertNotContains(response, 'No products.')

    def test_no_products(self):
        Product.objects.all().delete()
        response = self.client.get(reverse('products'))
        self.assertContains(response, 'No products.')
        self.assertEquals(len(response.context['products']), 0)
