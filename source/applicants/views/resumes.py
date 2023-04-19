from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from applicants.forms import ResumeForm
from applicants.models import Resume


class ResumeDetailView(DetailView):
    template_name = 'resumes/resume_detail.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        resume = get_object_or_404(Resume, pk=kwargs['pk'])
        if resume.is_deleted == True:
            raise Http404
        return context


class ResumeCreateView(CreateView):
    template_name = 'resumes/resume_create.html'
    model = Resume
    form_class = ResumeForm

    def get_success_url(self):
        return reverse('applicant_detail', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.applicant = self.request.user
        resume.save()
        return super().form_valid(form)


class ResumeUpdateView(UpdateView):
    template_name = 'resumes/resume_update.html'
    model = Resume
    form_class = ResumeForm

    def get_success_url(self):
        return reverse('applicant_detail', kwargs={'pk': self.request.user.pk})


class ResumeDeleteView(DeleteView):
    model = Resume

    def get_success_url(self):
        return reverse('applicant_detail', kwargs={'pk': self.request.user.pk})
