"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from junior.views import MainView, VacanciesListView, SpecializationView, CompanyCardView, VacancyView, \
    custom_handler_404, custom_handler_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesListView.as_view()),
    path('vacancies/cat/<str:category>/', SpecializationView.as_view()),
    path('companies/<int:id>/', CompanyCardView.as_view()),
    path('vacancies/<int:id>/', VacancyView.as_view()),
]

handler404 = custom_handler_404
handler500 = custom_handler_500
