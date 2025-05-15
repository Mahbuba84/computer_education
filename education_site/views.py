from django.shortcuts import render

def home(request):
    return render(request, 'education_site/index.html')