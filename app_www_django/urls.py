"""app_www_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wklejki import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('wklejki/', views.Wklejki_list.as_view()),
    path('wklejki/create',views.Wklejki_utworz.as_view()),
    path('wklejki/delete/<int:pk>', views.Wklejki_usun.as_view()),
    path('wklejki/update/<int:pk>', views.Wklejki_aktualizacja.as_view()),
    path('wklejki/lajk/<int:pk>', views.Wklejki_lajki.as_view()),
    path('wklejki/search/<int:pk>', views.Wklejki_list_by_user.as_view()),
]
