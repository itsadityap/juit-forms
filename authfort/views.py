from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = 'authfort/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('authfort:login')
