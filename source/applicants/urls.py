from django.urls import path

from applicants.views import ApplicantDetailView

urlpatterns = [
    path('applicant/<int:pk>/detail', ApplicantDetailView.as_view(), name='applicant_detail')
]
