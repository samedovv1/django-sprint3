from django.shortcuts import render


def about(request):
    """Отобразить страницу «О проекте»."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отобразить страницу «Наши правила»."""
    return render(request, 'pages/rules.html')
