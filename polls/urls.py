import mysite
import polls
from polls.views import home_screen, index
from django.urls import path
from .views import *

urlpatterns = [
    path('polls/', index, name='index'),
    path('', home_screen, name='home')
]
