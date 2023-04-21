from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from employers.forms import VacancyForm
from employers.models import Vacancy


class VacancyDetailView(DetailView):
    template_name = 'employers/vacancies/vacancy_detail.html'
    model = Vacancy

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        vacancy = get_object_or_404(Vacancy, pk=kwargs['pk'])
        if vacancy.is_deleted == True:
            raise Http404
        return context


class VacancyCreateView(CreateView):
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


class VacancyUpdateView(UpdateView):
    template_name = 'employers/vacancies/vacancy_update.html'
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        return reverse('employer_detail', kwargs={'pk': self.request.user.pk})


class VacancyDeleteView(DeleteView):
    model = Vacancy

    def get_success_url(self):
        return reverse('employer_detail', kwargs={'pk': self.request.user.pk})


def vacancy_update_data(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.updated_at = timezone.now()
    vacancy.save()
    return redirect('vacancy_detail', vacancy.pk)
