from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to retyurn the index page""" 

    return render(request, 'home/index.html')