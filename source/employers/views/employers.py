from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, FormView

from accounts.forms import AccountChangePasswordForm, AccountUpdateForm
from django.contrib.auth import get_user_model
from ..models import Vacancy


class EmployerDetailView(ListView):
    template_name = 'employers/employer_detail.html'
    model = Vacancy
    ordering = '-created_at'
    paginate_by = 3
    context_object_name = 'vacancies'

    def get_queryset(self):
        employer_id = self.kwargs.get('pk')
        return Vacancy.objects.filter(employer_id=employer_id).exclude(is_deleted=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employer = get_user_model().objects.get(pk=self.kwargs.get('pk'))
        context['employer_id'] = employer.id
        context['employer_email'] = employer.email
        context['employer_name'] = employer.name
        context['employer_phone'] = employer.phone
        context['employer_avatar'] = employer.avatar
        context['account_change_form'] = AccountUpdateForm(instance=employer)
        context['change_password_form'] = AccountChangePasswordForm(instance=employer)
        return context


class EmployerUpdateView(FormView):
    form_class = AccountUpdateForm

    def post(self, request, *args, **kwargs):
        employer = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        form = self.get_form_class()(request.POST, instance=employer)
        if form.is_valid():
            form.save()
        return redirect('employer_detail', pk=employer.pk)


class EmployerChangePasswordView(FormView):
    form_class = AccountChangePasswordForm

    def post(self, request, *args, **kwargs):
        employer = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        form = self.get_form_class()(request.POST, instance=employer)
        if form.is_valid():
            form.save()
        return redirect('applicant_detail', pk=employer.pk)
