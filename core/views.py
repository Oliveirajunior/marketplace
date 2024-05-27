from django.shortcuts import render


def index(request):
    return render(request, "app/index.html")


def contact(request):
    return render(request, "app/contact.html")
