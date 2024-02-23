from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MySocialUser

class MySocialUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', max_length=70)
    
    
    class Meta:
        model = MySocialUser
        fields = ['username', 'email', 'name', 'surnames', 'phone', 'profile_picture']
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        users = MySocialUser.objects.filter(username=username)
        if users.exists():
            raise ValueError("El nombre de usuario ya está en uso. Por favor, elige otro.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        emails = MySocialUser.objects.filter(email=email)
        if emails.exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    