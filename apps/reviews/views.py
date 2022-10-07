from django.views import generic
from apps.reviews.models import Reviews
from apps.users.models import Basket
from .forms import CreateReviewsForm
from django.shortcuts import redirect
from django.db.models import F
from django.urls import reverse_lazy

# Create your views here.

class CreateReviewsView(generic.CreateView):
    form_class = CreateReviewsForm
    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.user = self.request.user
        instance.product_id = self.kwargs['id']

        self.object = form.save()
        
        return redirect('single_page', self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        if request.method=='POST' and 'basket' in request.POST:
            # CreateBasketForm
            if not Basket.objects.filter(user = self.request.user, product_id = self.kwargs['id'], status = False):
                Basket.objects.create(user = self.request.user, product_id = self.kwargs['id'], quantity = request.POST.get('quantity'))
                return redirect('single_page', self.kwargs['id'])
            else:
                Basket.objects.filter(user = self.request.user, product_id = self.kwargs['id']).update(quantity = F("quantity") + request.POST.get('quantity'))
                return redirect('single_page', self.kwargs['id'])
        else:
            self.object = None
            return super().post(request, *args, **kwargs)

class DeleteRev(generic.DeleteView):
    model = Reviews
    template_name = 'home/site/delete.html'
    success_url = reverse_lazy('shop_cat')
    
    def form_valid(self, form):
        self.object.delete()
        return redirect('single_page', self.kwargs['id'])