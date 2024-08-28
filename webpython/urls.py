from django.urls import path
from webpython.views import show_webpython,show_nama

app_name = 'webpython'

urlpatterns = [
    path('apa/', show_webpython, name='show_webpython'),
     path('web', show_nama, name='show_nama'),
]
