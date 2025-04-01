from django.shortcuts import render


def home(request):
    #a = 10 / 0
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
