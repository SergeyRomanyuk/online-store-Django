from django.views.generic import CreateView
from .models import ContactForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactFRM


class ContactCreate(CreateView):
    model = ContactForm
    success_url = reverse_lazy('success_page')
    form_class = ContactFRM
    template_name ='contact_form.html'

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["tele"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'romanyuk.esa@gmail.com',
      ['romanyuk.esa@gmail.com']
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   return HttpResponse('Письмо отправлено!')
