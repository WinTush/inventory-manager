from django.shortcuts import render

from .models import Article


def home_view(request):
    context = {
        "title": "Home",
        "articles": Article.objects.all(),
    }
    return render(request, "articles/home.html", context=context)
