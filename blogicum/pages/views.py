"""Представления статических страниц."""

from django.shortcuts import render


def about(request):
    """Отображает страницу о проекте."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отображает страницу с правилами проекта."""
    return render(request, 'pages/rules.html')
