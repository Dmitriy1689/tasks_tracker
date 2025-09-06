from django.contrib.auth.forms import UserCreationForm
from tasks.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Форма создания пользователя."""
    class Meta(UserCreationForm.Meta):
        model = CustomUser
