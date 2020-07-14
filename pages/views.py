from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Create your views here.
def home_view(request,*args, **kwargs):
    return render(request, "home.html", {"a": "1"})


def contact_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 1337
    }
    return render(request, "about.html", my_context)