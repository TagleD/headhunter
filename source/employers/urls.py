from django.urls import path

from .views import EmployerDetailView, EmployerUpdateView, EmployerChangePasswordView

urlpatterns = [
    path('employers/<int:pk>/detail', EmployerDetailView.as_view(), name='employer_detail'),
    path('employers/<int:pk>/update', EmployerUpdateView.as_view(), name='employer_update'),
    path('employers/<int:pk>/change_password', EmployerChangePasswordView.as_view(), name='employer_change_password'),
]
