
from django.shortcuts import render





def  login(request):
    return render(request, 'homepage.html')
def  page_two(request):
    return render(request, 'home.html')
def  profile(request):
    return render(request, 'profile.html')