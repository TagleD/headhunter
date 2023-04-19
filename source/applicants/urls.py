from django.urls import path

from applicants.views.applicants import ApplicantDetailView, ApplicantUpdateView, ApplicantChangePasswordView
from applicants.views.resumes import ResumeCreateView, ResumeUpdateView, ResumeDetailView

urlpatterns = [
    # URL для Соискателя
    path('applicants/<int:pk>/detail', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('applicants/<int:pk>/update', ApplicantUpdateView.as_view(), name='applicant_update'),
    path('applicants/<int:pk>/change_password', ApplicantChangePasswordView.as_view(), name='applicant_change_password'),

    # URL для Резюме
    path('resumes/create', ResumeCreateView.as_view(), name='resume_create')
]
