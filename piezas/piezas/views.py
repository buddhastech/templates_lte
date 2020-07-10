from django.shortcuts import render


def top_nav(request):

    return render(request, 'base-top/index.html')

def collapse(request):

    return render(request, 'base-side/index.html')

def collapsed_top(request):

    return render(request, 'top-side/index.html')