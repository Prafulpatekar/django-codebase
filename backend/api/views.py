from django.shortcuts import render 
from django.http import JsonResponse

# Create your views here.

def api_hub(request):
    return JsonResponse({
        "message":"Hi there, Welcome to API-HUB!!❤️"
    })
