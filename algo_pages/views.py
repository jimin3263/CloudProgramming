from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'algo_pages/algorithm_page.html'
    )

def search(request):
    return render(
        request,
        'algo_pages/search.html'
    )