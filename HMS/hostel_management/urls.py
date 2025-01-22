from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hostel_create/', views.hostel_create, name='hostel_create'),
    path('hostel_list/', views.hostel_list, name='hostel_list'),
    path('<int:hostel_id>/',views.hostel_details, name='hostel_details'),
    path('<int:hostel_id>/hostel_edit/',views.hostel_edit, name='hostel_edit'),
    path('<int:hostel_id>/hostel_delete/',views.hostel_delete, name='hostel_delete'),
    path('room_create/', views.room_create, name='room_create'),
    path('room_list/', views.room_list, name='room_list'),
    path('<int:room_id>/room_std_list/', views.room_std_list, name='room_std_list'),
    path('<int:room_id>/room_edit/',views.room_edit, name='room_edit'),
    path('<int:room_id>/room_delete/',views.room_delete, name='room_delete'),

]