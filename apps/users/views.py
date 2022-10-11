from django.shortcuts import redirect
from apps.home_site.tasks import send_message
from django.contrib.auth import logout, login
from django.views import generic
from django.urls import reverse_lazy

from apps.services.models import Service
from apps.users.models import Basket, Order, User
from apps.construction.models import Pool
from django.contrib.auth.views import LoginView
from .forms import CreateBasketForm, LoginUserForm, RegisterUserForm, UpdateUserForm 


def logout_user(request):
    logout(request)
    return redirect('login_user')

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

class BasketViewList(generic.ListView):
    model = Basket 
    template_name = 'user/cart-page.html'
    context_object_name = 'basket'
    paginate_by = 10

    def get_context_data(self, *, odject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        total_p = 0
        for p in Basket.objects.filter(user_id = self.request.user.id, status = False):
            total_p += p.product.price * p.quantity

        context["total_p"] = total_p

        context['f'] = CreateBasketForm()
        return context 

    def get_queryset(self):
        products = Basket.objects.filter(user_id = self.request.user.id, status = False)
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
            text_for_admins = f"Здравствуйе, пользователь {self.request.user.username}-id: {self.request.user.id}; сделал заказ на сумму {all_price} сом \n почта: {self.request.user.email} \n номер: {self.request.user.phone} \n \n \n"
            for i in products:
                text_for_admins += f'-{i.product.title}:   {i.quantity} штук \n'

            send_message.delay(admins, text_for_admins)

            
            buy = Basket.objects.filter(user_id = self.request.user.id, status = False)
            order = Order.objects.create(user = self.request.user)
            order.save()
            for i in buy:
                i.order_set.add(order)
            Basket.objects.filter(user_id = self.request.user.id, status = False).update(status = True)


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

class ListUsers(generic.ListView):
    model = User 
    template_name = 'user/cart_page_users.html'
    context_object_name = 'users'
    paginate_by = 12    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['len_users'] = len(context['users'])
        return context

class DetailUser(generic.DetailView):
    model = User
    template_name = 'user/profile_for_admin.html'
    pk_url_kwarg = 'id'
    context_object_name = 'self_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user_id = self.kwargs['id'], active = True, received = False)
        context['services'] = Service.objects.filter(user_id = self.kwargs['id'], active = True)
        context['constructions'] = Pool.objects.filter(user_id = self.kwargs['id'], active = True)
        return context
        
class SearchUser(generic.ListView):
    paginate_by = 12
    template_name = 'user/cart_page_users.html'
    context_object_name = 'users'


    def get_queryset(self):
            return User.objects.filter(username__icontains = self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['len_users'] = len(context['users'])
        return context

class DetailUserForUser(generic.DeleteView):
    model = User
    template_name = 'user/profile_for_user.html'
    pk_url_kwarg = 'id'
    context_object_name = 'self_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user_id = self.kwargs['id'], active = True, received = False)
        context['services'] = Service.objects.filter(user_id = self.kwargs['id'], active = True)
        context['constructions'] = Pool.objects.filter(user_id = self.kwargs['id'], active = True)

        return context

    def post(self, request, *args, **kwargs):
        if request.method=='POST' and 'received' in request.POST:
            Order.objects.filter(id = request.POST.get('order_id')).update(received = True)
            return redirect('detail_user_for_user', self.kwargs['id'])
            
        elif request.method=='POST' and 'cancel_order' in request.POST:
            Order.objects.filter(id = request.POST.get('order_id')).update(cancel_order = True)
            return redirect('detail_user_for_user', self.kwargs['id'])

        elif request.method=='POST' and 'cancel_service' in request.POST:
            Service.objects.filter(id = request.POST.get('order_id')).update(cancel_service = True)
            return redirect('detail_user_for_user', self.kwargs['id'])

        elif request.method=='POST' and 'cancel_construction' in request.POST:
            Pool.objects.filter(id = request.POST.get('order_id')).update(cancel_construction = True)
            return redirect('detail_user_for_user', self.kwargs['id'])