from django.shortcuts import render, HttpResponse


# Create your views here.

def home_view(request):
    return render(request, "pages/index.html")


def shop_view(request):
    return HttpResponse("Страница категорий")


def product_detail(request, slug):
    return HttpResponse("Страница продукта")
