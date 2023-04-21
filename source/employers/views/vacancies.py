from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from ..forms import VacancyForm
from ..models import Vacancy


class ResumeDetailView(DetailView):
    template_name = 'employers/vacancies/vacancy_detail.html'
    model = Vacancy

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        vacancy = get_object_or_404(Vacancy, pk=kwargs['pk'])
        context['vacancy'] = vacancy
        return context


class ResumeCreateView(CreateView):
    template_name = 'employers/vacancies/vacancy_create.html'
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        return reverse('employer_detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        vacancy = form.save(commit=False)
        vacancy.employer = self.request.user
        vacancy.save()
        return super().form_valid(form)


class ResumeUpdateView(UpdateView):
    template_name = 'employers/vacancies/vacancy_update.html'
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        return reverse('applicant_detail', kwargs={'pk': self.request.user.pk})


class ResumeDeleteView(DeleteView):
    model = Vacancy

    def get_success_url(self):
        return reverse('applicant_detail', kwargs={'pk': self.request.user.pk})


def resume_update_data(request, pk):
    resume = get_object_or_404(Vacancy, pk=pk)
    resume.updated_at = timezone.now()
    resume.save()
    return redirect('vacancy_detail', resume.pk)
