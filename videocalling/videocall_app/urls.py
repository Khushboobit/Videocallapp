from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='Make Call'),
    path('logout/',views.logout_view, name='logout'),
    path('join/',views.Add_Call, name='Add_Call'),
    path('',views.index, name='index'),

]