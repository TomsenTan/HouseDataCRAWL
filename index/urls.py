from django.urls import path
from .views import *

urlpatterns = [
    path('about', about_views),
    path('addAuthor', add_author_views),
    path('getAuthor', get_author_views),
    path('select', select_views),
    path('addSecondHouse', add_secondHouse_msg)
]


