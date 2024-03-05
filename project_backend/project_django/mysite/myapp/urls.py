from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.details, name='details'),
    path('add_book/', views.add_book, name='add_book'),
    path('update/<int:book_id>/', views.update, name='update'),
    path('delete/<int:book_id>/', views.delete, name='delete'),
]