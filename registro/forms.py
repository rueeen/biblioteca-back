from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']        