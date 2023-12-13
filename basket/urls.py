from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_basket, name='basket'),
    path('add/<book_id>/', views.add_to_basket, name='add_to_basket'),
]