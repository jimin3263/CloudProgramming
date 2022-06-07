from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'algo_today/algorithm_today.html'
    )