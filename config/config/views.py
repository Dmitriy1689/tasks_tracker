from django.urls import reverse_lazy
from django.views.generic import CreateView
from config.forms import CustomUserCreationForm


class SignUpView(CreateView):
    """Представление для регистрации нового пользователя."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
