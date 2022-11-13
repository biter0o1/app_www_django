from django.urls import path
from . import views

urlpatterns = [
    path('', views.osoba_list),
    path('create', views.osoba_create),
    path('<int:pk>/', views.osoba_detail),
]
