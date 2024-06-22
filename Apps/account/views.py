from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, TemplateView

from .forms import CustomLoginForm


# Create your views here.
class LoginPage(TemplateView):
    template_name = 'login.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomLoginForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CustomLoginForm(request.POST, request=request)
        if form.is_valid():
            return redirect('/')
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
