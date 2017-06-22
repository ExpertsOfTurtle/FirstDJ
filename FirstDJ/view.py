from django.shortcuts import render

def hello(request):
    context          = {}
    context['dfsname'] = 'DFS'
    return render(request, 'login.html', context)