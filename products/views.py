from django.shortcuts import render

from .forms import ProductForm

from .models import Product
#Show one product
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "product/products_create.html", context)




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
    return render(request, "products/detail.html", context)
 