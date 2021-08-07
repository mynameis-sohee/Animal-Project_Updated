from django.shortcuts import render, redirect

# Create your views here.

def main_view(request):
    return render(request, 'main.html')


def about_view(request):
    return render(request, 'about.html')