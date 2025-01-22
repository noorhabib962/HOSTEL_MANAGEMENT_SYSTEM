from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student_create/', views.student_create, name='student_create'),
    path('student_list/', views.student_list, name='student_list'),
    path('<int:student_id>/student_edit/',views.student_edit, name='student_edit'),
    path('<int:student_id>/student_delete/',views.student_delete, name='student_delete'),

]