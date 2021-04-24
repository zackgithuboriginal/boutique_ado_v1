from django.shortcuts import render


# Create your views here.
def view_bag(request):
    """ A view to retyurn the bag contens page""" 

    return render(request, 'bag/bag.html')