from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def get_involved(request):
    return render(request, 'home/get_involved.html')
