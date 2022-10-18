from django.db import models
from web.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ваше имя')
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name='Адрес доставки')
    tel = models.CharField(max_length=20, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Самовывоз', default='Да/Нет')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE,verbose_name='Наименование' )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
