from django.shortcuts import render
from django.http  import HttpResponse
from . models import Images

# Create your views here.

# Create your views here.
def welcome(request):
    photos = Images.objects.all()
    # return HttpResponse('Welcome My Gallery.')
    return render(request, 'all-news/index.html',{'photos':photos})

def search_images(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any Category"
        return render(request, 'all-news/search.html',{"message":message})