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
    
def landing(request):
    all_images = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
    title = 'Home'

    return render(request,'index.html', {'all_images':all_images,'location':location,'category':category, 'title':title})


def page_location(request,location):
    location = Location.objects.all()
    category = Category.objects.all()
    title = f"{location}"
    location_results = Image.filter_location(location)
    return render(request,'index.html',{'all_images':location_results,'location':location,'category':category, 'title':title})    
    
# def article(request,article_id):
#     try:
#         article = Article.objects.get(id = article_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-news/article.html", {"article":article})    

