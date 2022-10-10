from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import *
from apps.services.models import Service
from apps.shop.models import ImagesForProducts
from apps.users.models import Basket, Order
from apps.home_site.models import ConstructionImages, SiteInfo
from apps.construction.models import Pool


class Home(generic.ListView):
    model = SiteInfo 
    template_name = 'home/home.html'

class UpdateInfo(generic.UpdateView):
    model = SiteInfo
    form_class = UpdateOrCreateInfoForm
    template_name = 'home/site/update_info.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save(commit=False)
        self.object = form.save()
        images = self.request.FILES.getlist('filefield')
        for img in images:
            ConstructionImages.objects.create(image = img)
        return redirect('update_info', '1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ConstructionImages.objects.all()
        context['id'] = self.kwargs['pk']
        return context

class Admin(generic.ListView):
    model = SiteInfo 
    template_name = 'home/site/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(active = False)
        context['services'] = Service.objects.filter(active = False)
        context['constructions'] = Pool.objects.filter(active = False)
        return context
    
    def post(self, request, *args, **kwargs):
        if request.method=='POST' and 'active_buy' in request.POST:
            Order.objects.filter(id = request.POST.get('order_id')).update(active = True)
            return redirect('admin')
        elif request.method=='POST' and 'active_ser' in request.POST:
            Service.objects.filter(id = request.POST.get('service_id')).update(active = True)
            return redirect('admin')
        elif request.method=='POST' and 'active_pool' in request.POST:
            Pool.objects.filter(id = request.POST.get('pool_id')).update(active = True)
            return redirect('admin')

class CreateProduct(generic.CreateView):
    form_class = CreateProductForm
    template_name = 'home/site/create_product.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        self.object = form.save()
        images = self.request.FILES.getlist('filefield')
        for img in images:
            ImagesForProducts.objects.create(product = instance, image = img)
        return redirect('single_page', instance.id)

class CreateCatProduct(generic.CreateView):
    form_class = CreateCatProductForm
    template_name = 'home/site/yes.html'
    success_url = reverse_lazy('home')

class CreateTypePool(generic.CreateView):
    form_class = CreateTypePoolForm
    template_name = 'home/site/yes.html'
    success_url = reverse_lazy('home')

class CreatePoolAdditionally(generic.CreateView):
    form_class = CreatePoolAdditionallyForm
    template_name = 'home/site/yes.html'
    success_url = reverse_lazy('home')

class CreatePoolDecoration(generic.CreateView):
    form_class = CreatePoolDecorationForm
    template_name = 'home/site/yes.html'
    success_url = reverse_lazy('home')

class CreateServiceType(generic.CreateView):
    form_class = CreateServiceTypeForm
    template_name = 'home/site/yes.html'
    success_url = reverse_lazy('home')

class DeleteImage(generic.DeleteView):
    model = ConstructionImages
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('update_info')
    
    def form_valid(self, form):
        self.object.delete()
        return redirect('update_info', '1')

class DeleteOrder(generic.DeleteView):
    model = Order
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('admin')
    
    def form_valid(self, form):
        order = Order.objects.get(id = self.kwargs['pk'])
        Basket.objects.filter(user = order.user, status = True, order = order).delete()
        self.object.delete()
        return redirect('admin')

class DeleteOrderUser(generic.DeleteView):
    model = Order
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('admin')
    
    def form_valid(self, form):
        order = Order.objects.get(id = self.kwargs['pk'])
        Basket.objects.filter(user = order.user, status = True, order = order).delete()
        self.object.delete()
        return redirect('detail_user', self.kwargs['id'])

class DeleteServiceUser(generic.DeleteView):
    model = Service
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('admin')
    
    def form_valid(self, form):
        self.object.delete()
        return redirect('detail_user', self.kwargs['id'])

class DeleteService(generic.DeleteView):
    model = Service
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('admin')

class DeletePool(generic.DeleteView):
    model = Pool
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('admin')

class DeletePoolUser(generic.DeleteView):
    model = Pool
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('admin')
    
    def form_valid(self, form):
        self.object.delete()
        return redirect('detail_user', self.kwargs['id'])