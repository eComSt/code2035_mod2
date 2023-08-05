from django.shortcuts import render
from .models import Advertisement
def index(request):
    adv = Advertisement.objects.all()
    context = {
        'advertisements': adv
    }
    return render(request, 'index.html',context)
def top_sellers(request):
    return render(request, 'top-sellers.html')