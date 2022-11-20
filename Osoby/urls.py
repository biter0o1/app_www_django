from django.urls import path
from . import views

urlpatterns = [
    path('', views.OsobaGet.as_view()),
    path('create', views.OsobaCreate.as_view()),
    path('update/<int:pk>', views.OsobaUpdate.as_view()),
    path('delete/<int:pk>', views.OsobaDelete.as_view()),
    path('<int:pk>/', views.OsobaGetOne.as_view()),
]
