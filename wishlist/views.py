from django.shortcuts import render
from wishlist.models import BarangWishlist

def show_wishlist(request):
    return render(request, "wishlist.html")

def show_data(request):
    data = BarangWishlist.objects.all()
    context = {
    'list_barang': data,
    'nama': 'Kak Cinoy'
    }
    print(data)
    return render(request,"wishlist.html",context)
# Create your views here.
