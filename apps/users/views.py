from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from apps.users.models import Basket, User
from apps.home_site.tasks import send_message
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


class RegistrationView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)   
        return redirect('update_profile', self.request.user.id)

class LoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class BasketViewList(generic.ListView):
    model = Basket 
    template_name = 'user/cart-page.html'
    context_object_name = 'basket'
    paginate_by = 10

    def get_context_data(self, *, odject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total_p = 0
        for p in Basket.objects.filter(user_id = self.request.user.id):
            total_p += p.product.price * p.quantity

        context["total_p"] = total_p

        context['f'] = CreateBasketForm()
        return context 

    def get_queryset(self):
        products = Basket.objects.filter(user_id = self.request.user.id)
        return products

    def post(self, request, *args, **kwargs):
        if request.method=='POST' and 'basket' in request.POST:
            if int(request.POST.get('quantity')) > 0:
                Basket.objects.filter(user = self.request.user, product_id = request.POST.get('product_id')).update(quantity = request.POST.get('quantity'))
            return redirect('basket')

        elif request.method=='POST' and 'del_basket' in request.POST:
            Basket.objects.filter(id = request.POST.get('basket_id')).delete()
            return redirect('basket')   
        elif request.method=='POST' and 'buy' in request.POST:
            products = Basket.objects.filter(user_id = self.request.user.id)
            all_price = 0

            admins = []
            for i in User.objects.filter(is_staff = True):
                admins.append(i.email)

            for i in products:
                all_price += i.product.price * i.quantity
            text = f"Здравствуйе, вы сделали заказ на сумму {all_price} сом \n \n \n"
            text_for_admins = f"Здравствуйе, пользователь {self.request.user.username}-id: {self.request.user.id}; сделал заказ на сумму {all_price} сом \n почта: {self.request.user.email} \n номер: {self.request.user.phone} \n \n \n"
            for i in products:
                text += f'-{i.product.title}:   {i.quantity} штук \n'
                text_for_admins += f'-{i.product.title}:   {i.quantity} штук \n'

            send_message.delay([self.request.user.email], text)
            send_message.delay(admins, text_for_admins)

            Basket.objects.filter(user_id = self.request.user.id).delete()

            return redirect('basket')

class UpdateProfile(generic.UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'user/profile.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner'] = self.kwargs['pk']
        context['owner_user'] = User.objects.get(id = self.kwargs['pk'])
        return context

            
    def form_valid(self, form):
        self.object = form.save()
        return redirect('update_profile', self.kwargs['pk'])
