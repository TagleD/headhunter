from django.urls import path

from .views import EmployerDetailView, EmployerUpdateView, EmployerChangePasswordView, VacancyCreateView, \
    VacancyDetailView, VacancyUpdateView, VacancyDeleteView, vacancy_update_data

urlpatterns = [
    # URL для Работодателя
    path('employers/<int:pk>/detail', EmployerDetailView.as_view(), name='employer_detail'),
    path('employers/<int:pk>/update', EmployerUpdateView.as_view(), name='employer_update'),
    path('employers/<int:pk>/change_password', EmployerChangePasswordView.as_view(), name='employer_change_password'),

    # URL для Резюме
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancies/<int:pk>/detail/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancies/<int:pk>/delete/', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('vacancies/<int:pk>/update_data', vacancy_update_data, name='vacancy_update_data')
]
