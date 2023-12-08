from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Product, Order

# Create your views here.


class HomeListView(ListView):
    template_name = 'home.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 50


class CartView(TemplateView):
    template_name = 'my_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        order = Order.objects.filter(user=user).first()
        context['order'] = order
        return context
