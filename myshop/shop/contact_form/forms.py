from django.forms import ModelForm
from django.forms import Textarea
from .models import ContactForm


class ContactFRM(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = ContactForm
        # Поля, которые будем использовать для заполнения
        fields = ['first_name', 'tele', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            )
        }