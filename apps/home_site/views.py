
from django.views import generic
from django.shortcuts import redirect
from .forms import *
from django.urls import reverse_lazy



from apps.home_site.models import ConstructionImages, SiteInfo


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
        instance = form.save(commit=False)
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