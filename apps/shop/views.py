from apps.home_site.forms import CreateProductForm
from apps.reviews.models import Reviews
from apps.reviews.views import *
from apps.shop.models import *
from django.views import generic
from django.core.paginator import Paginator
from apps.users.forms import CreateBasketForm
from django.urls import reverse_lazy


# Create your views here.

def cat_sort(id):
    list = [id]
    if not Category.objects.filter(parent_id = id):
        return list
    else:
        cat = Category.objects.filter(parent_id = id)
        
    for i in cat:
        list.append(i.id)
        if not Category.objects.filter(parent_id = i.id):
            pass
        else:
            list.extend(cat_sort(i.id))

    return list

class SingleProduct(CreateReviewsView, generic.DetailView):
    model = Product
    template_name = 'shop/single_page.html'
    pk_url_kwarg = 'id'
    context_object_name = 'product'

    def get_context_data(self, *, odject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']

        context['images'] = ImagesForProducts.objects.filter(product_id = id)
        context['id'] = id

        context['f'] = CreateBasketForm()

        reviews = Reviews.objects.filter(product_id = id)

        all_rev = 0

        for r in reviews:
            all_rev += r.rating

        if all_rev == 0:
            context['all_rev'] = 0
            context['len_r'] = 'нет'
        else:
            context['all_rev'] = all_rev / len(reviews)
            context['len_r'] = len(reviews)


        context['rev_len'] = [0.5, 1.5, 2.5, 3.5, 4.5]



        paginator = Paginator(reviews, 5)
        page_number = self.request.GET.get('page')
        context['reviews'] = paginator.get_page(page_number)
        context['page_obj'] = paginator.get_page(page_number)
        context['paginator'] = paginator
        

        
        return context

class ShopCat(generic.ListView):
    model = Product 
    template_name = 'shop/shop_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, *, odject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cat'] = Category.objects.all()
        cat_id = self.kwargs['id']
        # if cat_id != 0:
        #     context['categ'] = Category.objects.get(pk = cat_id)
        context['cat_id'] = cat_id
        context['fiter_len'] = len(Product.objects.all())
        context['all_len'] = len(Product.objects.all())

        return context 

    def get_queryset(self):

        id = self.kwargs['id']

        if id != 0:
            cat_list = cat_sort(id)
            products = Product.objects.filter(category_id__in = cat_list)
        else:
            products = Product.objects.all()

        return products

    def get_sorted(self):
        a = {
            'По возростанию цены': 'price',
            'По убыванию цены': '-price'
        }
        return a

class FilterPrice(ShopCat, generic.ListView):
    
    template_name = "shop/shop_list.html"
    context_object_name = 'products'
    paginate_by = 1000

    def get_queryset(self):
        id = self.kwargs['id']

        if self.request.GET.get("min_p") == '':
            max_p = 1000000000
        else:
            max_p = self.request.GET.get("min_p")

        if self.request.GET.get("max_p") == '':
            min_p = 0
        else:
            min_p = self.request.GET.get("max_p")


        if id != 0:
            cat_list = cat_sort(id)
            queryset = Product.objects.filter(price__gte = min_p, price__lte = max_p, category_id__in = cat_list).order_by(self.request.GET.get("sorted"))
        else:
            queryset = Product.objects.filter(price__gte = min_p, price__lte = max_p).order_by(self.request.GET.get("sorted"))

        return queryset

    def get_context_data(self, *, odject_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['fiter_len'] = len(context['products'])
        context['all_len'] = len(Product.objects.filter(category_id__in = cat_sort(self.kwargs['id'])))

        context['max_p'] = self.request.GET.get('max_p')
        context['min_p'] = self.request.GET.get('min_p')

        return context 

class Search(generic.ListView):
    paginate_by = 12
    template_name = 'shop/shop_list.html'
    context_object_name = 'products'


    def get_queryset(self):
        if self.kwargs['id'] != 0:
            return Product.objects.filter(title__icontains = self.request.GET.get('q'), category_id = self.kwargs['id'])
        else:
            return Product.objects.filter(title__icontains = self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')

        context['cat'] = Category.objects.all()
        context['cat_id'] = self.kwargs['id']
        context['fiter_len'] = len(Product.objects.all())
        context['all_len'] = len(Product.objects.all())

        return context

    def get_sorted(self):
        a = {
            'По возростанию цены': 'price',
            'По убыванию цены': '-price'
        }
        return a

class UpdateProduct(generic.UpdateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'home/site/create_product.html'
    context_object_name = 'form'

    def form_valid(self, form):
        instance = form.save(commit=False)
        self.object = form.save()
        images = self.request.FILES.getlist('filefield')
        for img in images:
            ImagesForProducts.objects.create(product = instance, image = img)
        return redirect('single_page', instance.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ImagesForProducts.objects.filter(product = self.kwargs['pk'])
        context['id'] = self.kwargs['pk']
        return context

class DeleteImageProduct(generic.DeleteView):
    model = ImagesForProducts
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('update_product')
    
    def form_valid(self, form):
        self.object.delete()
        return redirect('update_product', self.kwargs['id'])

class DeleteProduct(generic.DeleteView):
    model = Product
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('shop_cat')
    
    def form_valid(self, form):
        self.object.delete()
        return redirect('shop_cat', '0')

