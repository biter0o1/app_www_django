from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.osoba_list),
    path('<int:pk>/', views.osoba_detail),
]