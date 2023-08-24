from django.shortcuts import render

# Create your views here.


def home_page(request):
    content = {}
    return render(request, "home.html", content)
