from django.urls import path

from applicants.views import ApplicantDetailView, ApplicantUpdateView, ApplicantChangePasswordView

urlpatterns = [
    path('applicant/<int:pk>/detail', ApplicantDetailView.as_view(), name='applicant_detail'),
    path('applicant/<int:pk>/update', ApplicantUpdateView.as_view(), name='applicant_update'),
    path('applicant/<int:pk>/change_password', ApplicantChangePasswordView.as_view(), name='applicant_change_password')
]
