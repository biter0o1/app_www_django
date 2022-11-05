from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.OsobaList.as_view()),
    path('<int:pk>/', views.OsobaDetail.as_view()),
]