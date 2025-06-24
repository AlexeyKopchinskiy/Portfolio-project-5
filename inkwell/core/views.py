from django.shortcuts import render


def start_page(request):
    return render(request, "start.html")


def about_page(request):
    return render(request, "about.html")


def cookies_page(request):
    return render(request, "cookies.html")


def terms_page(request):
    return render(request, "terms.html")


def prices_page(request):
    return render(request, "prices.html")
