from django.urls import path

from .views import RegisterAccountView

urlpatterns = [
    path('register/', RegisterAccountView.as_view(), name='register'),
]

