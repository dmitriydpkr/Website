from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    n = ['Oleg', 'Vasya',2,4]
    return render(request, 'blog/index.html', context={'names':n})



