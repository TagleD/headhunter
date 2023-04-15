from django.views.generic import ListView

from accounts.models import Account
from applicants.models import Resume


# Create your views here.


class ApplicantDetailView(ListView):
    template_name = 'applicants/applicant_detail.html'
    model = Resume
    ordering = ('-created_at',)
    paginate_orphans = 1
    paginate_by = 4

    def get_queryset(self):
        applicant_id = self.kwargs.get('pk')
        return Resume.objects.filter(applicant_id=applicant_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applicant = Account.objects.get(pk=self.kwargs.get('pk'))
        context['user_email'] = applicant.email
        context['user_name'] = applicant.name
        context['user_phone'] = applicant.phone
        context['user_avatar'] = applicant.avatar
        return context
