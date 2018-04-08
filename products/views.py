from django.views import generic
from models import *


class IndexView(generic.ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_list.html'
