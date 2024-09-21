from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='homepage'),
    path('home/', views.page_two, name='home'),

    path('profile/', views.profile, name='profile'),


]



