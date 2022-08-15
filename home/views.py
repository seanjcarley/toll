from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    ''' view to return index.html '''
    # return HttpResponse("Hello, world. This is the home index")
    return render(request, 'home/index.html')