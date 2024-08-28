from django.urls import path
from wishlist.views import show_wishlist, show_data

app_name = 'wishlist'

urlpatterns = [
    path('ini', show_wishlist, name='show_wishlist'),
    path("pbp",show_data, name = "show_data")
]