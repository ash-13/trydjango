from django.shortcuts import render
from .models import product

# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'desciption' : obj.desciption
    }
    request render(request, "product/detail.html", {})
