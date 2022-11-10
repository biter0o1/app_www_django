from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.osoba_list),
    path('create', views.osoba_create),
    path('<int:pk>/', views.osoba_detail),
    path('<int:pk>/', views.osoba_get_one),
]