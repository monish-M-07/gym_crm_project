from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('members/', views.members_list, name='members_list'),
    path('members/add/', views.add_member, name='add_member'),
    path('fees/', views.fees_list, name='fees_list'),
    path('fees/add/', views.add_fee, name='add_fee'),
]
