from .models import MySocialUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class MySocialUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=75, label="Nombre de Usuario", widget= forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(max_length=75, label="Email", widget= forms.EmailInput(attrs={"class":"form-control"}))
    name = forms.CharField(max_length=75, label="Nombre", widget= forms.TextInput(attrs={"class":"form-control"}))
    surnames = forms.CharField(max_length=75, label="Apellidos", widget= forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(max_length=10, label="Numero de Telefono", widget= forms.TextInput(attrs={"class":"form-control"}))
    profileimg = forms.ImageField(label="Seleccionar imagen", widget= forms.FileInput())
    password1 = forms.CharField(label='Contraseña', max_length=18, widget= forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label='Confirmar Contraseña', max_length=18, widget= forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = MySocialUser
        fields = ['username', 'email', 'name', 'surnames', 'phone', 'profileimg','password1','password2']
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if MySocialUser.objects.filter(username=username).exists():
            raise forms.ValidationError("El nombre de usuario ya está en uso. Por favor, elige otro.")
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
    