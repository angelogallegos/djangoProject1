from django.urls import path
from polls import  views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('index/', views.index, name='index')
]