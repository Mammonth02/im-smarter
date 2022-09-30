from django.views import generic
from django.shortcuts import redirect
from apps.services.models import *
from apps.users.models import User
from apps.home_site.tasks import send_message


# Create your views here.
class ServicesListView(generic.ListView):
    model = ServiceType 
    template_name = 'services/services.html'
    context_object_name = 'services'

class ServiceView(generic.DetailView):
    model = ServiceType
    template_name = 'services/service.html'
    pk_url_kwarg = 'id'
    context_object_name = 'service'


    def post(self, request, *args, **kwargs):
        if request.method=='POST' and 'send_m' in request.POST:
            admins = []
            for i in User.objects.filter(is_staff = True):
                admins.append(i.email)
            text_for_admins = f"Здравствуйе, пользователь {request.POST.get('name')} \n почта: {request.POST.get('email')} \n номер: {request.POST.get('phonenumber')} \n \n \n Отправил сообшение: {request.POST.get('message')}"
            send_message.delay(admins, text_for_admins)
            return redirect('service', self.kwargs['id'])
        elif request.method=='POST' and 'serv' in request.POST:
            obj = Service.objects.create(user = self.request.user, category_id = self.kwargs['id'], message = request.POST.get('message'))
            admins = []
            for i in User.objects.filter(is_staff = True):
                admins.append(i.email)
            text_for_admins = f"Здравствуйе, пользователь {self.request.user.username}-id: {self.request.user.id}; \n почта: {self.request.user.email} \n номер: {self.request.user.phone} \n \n \n Заказал услугу\n Катигория: {obj.category} \n Сообшение: {obj.message} "
            send_message.delay(admins, text_for_admins)
            return redirect('service', self.kwargs['id'])


