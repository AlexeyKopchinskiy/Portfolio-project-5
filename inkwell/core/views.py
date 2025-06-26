from django.shortcuts import render
from blog.models import Post


def start_page(request):
    latest_posts = Post.objects.filter(published=True).order_by("-created_at")[
        :4
    ]
    return render(request, "start.html", {"latest_posts": latest_posts})


def about_page(request):
    return render(request, "about.html")


def cookies_page(request):
    return render(request, "cookies.html")


def terms_page(request):
    return render(request, "terms.html")


def prices_page(request):
    return render(request, "prices.html")
