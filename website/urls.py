from django.urls import path
from .views import *

urlpatterns = [
    path(r'mainPage', mainpage_views),

]