from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import CustomAccountCreationForm


# Create your views here.

class RegisterAccountView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = CustomAccountCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            account = form.save()
            account.username = None
            account.save()
            login(request, account)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)

