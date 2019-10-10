from django.shortcuts import render
from django.http  import HttpResponse
from . models import Images

# Create your views here.

# Create your views here.
def welcome(request):
    photos = Images.objects.all()
    # return HttpResponse('Welcome My Gallery.')
    return render(request, 'all-news/home.html',{'photos':photos})
