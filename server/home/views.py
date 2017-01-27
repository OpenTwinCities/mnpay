from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
@xframe_options_exempt
def index(request):
    return render(request, 'home/index.html')


@xframe_options_exempt
def get_involved(request):
    return render(request, 'home/get_involved.html')
