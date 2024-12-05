from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    passhash = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'input__item',  # Clases CSS personalizadas
        }),
        label='',  # Ocultar etiqueta predeterminada
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'passhash']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'username': forms.TextInput(attrs={'placeholder': 'Your Name'}),
        }
