from django.views import generic
from allauth.account.views import SignupView, LoginView, PasswordResetView

# Create your views here.
class home(generic.TemplateView):
    template_name = 'home/home.html'

class MyLoginView(LoginView):
    template_name = 'allauth/accounts/login.html'