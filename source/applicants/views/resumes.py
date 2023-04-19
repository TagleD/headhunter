from django.urls import reverse
from django.views.generic import CreateView

from applicants.forms import ResumeForm
from applicants.models import Resume


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