from django.db.models import Count
from django.shortcuts import render
from django.views import View

from junior.models import Vacancy, Company


class MainView(View):
    def get(self, request):
        vacancies = Vacancy.objects.values('specialty__code', 'specialty__title', 'specialty__picture').\
            annotate(count=Count('specialty__title'))
        companies = Vacancy.objects.values('company__id', 'company__logo').annotate(count=Count('company__name'))
        context = {
            'vacancies': vacancies,
            'companies': companies,
        }
        return render(request, 'junior/index.html', context)


class VacanciesListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'junior/vacancies.html', context)


class SpecializationView(View):
    def get(self, request, category):
        vacancies = Vacancy.objects.filter(specialty__code=category)
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'junior/vacancies.html', context)


class CompanyCardView(View):
    def get(self, request, id):
        company = Company.objects.get(pk=id)
        vacancies = Vacancy.objects.filter(company__name=company.name)
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'company': company,
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'junior/company.html', context)


class VacancyView(View):
    def get(self, request, id):
        vacancy = Vacancy.objects.get(pk=id)
        vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancy': vacancy,
        }
        return render(request, 'junior/vacancy.html', context)


def custom_handler_404(request, exception):
    return render(request, 'junior/error_404.html')


def custom_handler_500(request):
    return render(request, 'junior/error_500.html')
