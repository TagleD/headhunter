from django.contrib.auth import login, authenticate, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import View, CreateView, TemplateView

from .forms import CustomAccountCreationForm, LoginForm


class LoginView(SuccessMessageMixin, TemplateView):
    template_name = 'accounts/login.html'
    form = LoginForm
    success_message = 'Вы успешно зашли в систему'

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        account = authenticate(request=request, email=email, password=password)

        if not account:
            return redirect('login')

        # Login User(Account)
        login(request, account)

        return redirect('index')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')



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

