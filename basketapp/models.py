from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)

    def totalsum(self):
        total_sum = 0
        for item in self:
            total_sum += item.product.price * item.quantity
        return total_sum

    def totalqnt(self):
        total_qnt = 0
        for item in self:
            total_qnt += item.quantity
        return total_qnt
