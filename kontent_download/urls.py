# urls.py fayli (kontent_download app)
from django.urls import path
from . import views

app_name = "kontent_download"

urlpatterns = [
    path('', views.index, name='index'),
]


