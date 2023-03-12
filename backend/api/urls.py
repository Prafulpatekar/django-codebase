from django.urls import path 
from . import views

urlpatterns = [
    path('',views.api_hub,name='api_hub')
]
