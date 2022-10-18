from django.db import models


class ContactForm(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Ваше имя')
    tele=models.IntegerField(max_length=200, verbose_name='Номер телефона')
    email = models.EmailField(max_length=200, verbose_name='Email')
    message = models.TextField(max_length=1000, verbose_name='Сообщение')

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email
