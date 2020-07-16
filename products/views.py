from django.shortcuts import render

from .models import Product
#Show one product
def product_detail_view(request):
    #Below isn't an actual error it's just needs Django aware PyLint
    obj = Product.objects.get(id=2)
    #context = {
    #    "title": obj.title,
    #    "description": obj.description
    #}

    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)
 