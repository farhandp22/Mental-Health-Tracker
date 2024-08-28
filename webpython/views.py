from django.shortcuts import render
from wishlist.models import BarangWishlist


# Create your views here.
def show_webpython(request):
    return render(request, "webpython.html")

def show_nama(request):
    data = BarangWishlist.objects.all()
    context= {
        'nama' : "Farhan",
        'data' : data
    }
    
    return render(request,"webpython.html", context)