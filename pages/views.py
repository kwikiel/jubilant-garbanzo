from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "home.html", {"a": "1"})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Hello Contact</h1>")