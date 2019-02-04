from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def posts_list(request):
    names = ['Oleg', 'Sergey', 'Masha', 'Leonid']
    return render(request, 'blog/index.html', context={'names': names})
