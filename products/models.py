from django.core.exceptions import ValidationError
from django.db.models import *


# Create your models here.
class Product(Model):
    name = CharField(max_length=128)
    price = IntegerField()
    stock_count = IntegerField()

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price negative')

        if self.stock_count < 0:
            raise ValidationError('Stock negative')

    def get_discounted_price(self, discount):
        return self.price * (1 - discount / 100)

    def total_value(self):
        return self.price * self.stock_count

    def __str__(self):
        return self.name