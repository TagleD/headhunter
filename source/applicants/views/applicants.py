from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, FormView

from accounts.forms import AccountChangePasswordForm, AccountUpdateForm
from accounts.models import Account
from applicants.models import Resume


# Create your views here.


class ApplicantDetailView(ListView):
    template_name = 'applicants/applicant_detail.html'
    model = Resume
    ordering = ('-created_at',)
    paginate_orphans = 1
    paginate_by = 3

    def get_queryset(self):
        applicant_id = self.kwargs.get('pk')
        return Resume.objects.filter(applicant_id=applicant_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applicant = Account.objects.get(pk=self.kwargs.get('pk'))
        context['applicant_id'] = applicant.id
        context['applicant_email'] = applicant.email
        context['applicant_name'] = applicant.name
        context['applicant_phone'] = applicant.phone
        context['applicant_avatar'] = applicant.avatar
        context['account_change_form'] = AccountUpdateForm(instance=applicant)
        context['change_password_form'] = AccountChangePasswordForm(instance=applicant)
        return context


class ApplicantUpdateView(FormView):
    form_class = AccountUpdateForm

    def post(self, request, *args, **kwargs):
        applicant = get_object_or_404(Account, pk=self.kwargs.get('pk'))
        form = self.get_form_class()(request.POST, instance=applicant)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('applicant_detail', pk=applicant.pk)


class ApplicantChangePasswordView(FormView):
    form_class = AccountChangePasswordForm

    def post(self, request, *args, **kwargs):
        applicant = get_object_or_404(Account, pk=self.kwargs.get('pk'))
        form = self.get_form_class()(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
        return redirect('applicant_detail', pk=applicant.pk)
