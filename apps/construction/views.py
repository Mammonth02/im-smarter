from multiprocessing import context
from apps.construction.forms import CreatePoolForm
from django.urls import reverse_lazy

from apps.home_site.models import ConstructionImages
from .models import *
from django.views import generic
from django.shortcuts import redirect
from apps.home_site.tasks import send_message




# Create your views here.

class cListView(generic.CreateView):
    form_class = CreatePoolForm
    template_name = 'construction/construction.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        if instance.width > 0 and instance.length > 0 and instance.depth > 0:
            self.object = form.save()

            pool = Pool.objects.get(id = instance.id)

            pool = [str(i).split(':') for i in pool.additionally.all()]
            

            text = f"Здравствуйе, вы сделали заказ для строительства бассейна\n \n \n -тип: {instance.category} \n -ширина: {instance.width} \n -длина: {instance.length} \n -глубина: {instance.depth} \n -отделка: {instance.decoration} \n -дополнительно: {pool} \n -коментарий: {instance.desctiption} \n \n \n"
            text_for_admins = f"Здравствуйе, пользователь {self.request.user.username}-id: {self.request.user.id}; заказал бассейн \n почта: {self.request.user.email} \n номер: {self.request.user.phone} \n \n \n -тип: {instance.category} \n -ширина: {instance.width} \n -длина: {instance.length} \n -глубина: {instance.depth} \n -отделка: {instance.decoration} \n -дополнительно: {pool} \n -коментарий: {instance.desctiption} \n \n \n"
            
            admins = []
            for i in User.objects.filter(is_staff = True):
                admins.append(i.email)

            send_message.delay([self.request.user.email], text)
            send_message.delay(admins, text_for_admins)

        return redirect('construction')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ConstructionImages.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        if request.method=='POST' and 'send_m' in request.POST:
            admins = []
            for i in User.objects.filter(is_staff = True):
                admins.append(i.email)
            text_for_admins = f"Здравствуйе, пользователь {request.POST.get('name')} \n почта: {request.POST.get('email')} \n номер: {request.POST.get('phonenumber')} \n \n \n Отправил сообшение: {request.POST.get('message')}"
            send_message.delay(admins, text_for_admins)
            return redirect('home')
        self.object = None
        return super().post(request, *args, **kwargs)
