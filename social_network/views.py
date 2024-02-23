from django.shortcuts import render, redirect
from .forms import MySocialUserCreationForm
from .models import MySocialUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success, error
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from dotenv import load_dotenv
from services import email_service


load_dotenv("settings.py")

User = get_user_model()

def signin(request):
    if request.method == "GET":
        
        return render(request, "signup&login/signin.html", {"form":AuthenticationForm})

    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                
        if user is None:
            error(request, message="El usuario o la contraseña es incorrecta")
            return render(request, "signup&login/signin.html", {"form":AuthenticationForm})
        else:
            login(request, user)
            return redirect("home")

def siqnout(request):
    logout(request)
    return redirect("signin")

def activate_account(request, activation_token):
    try:
        users = User.objects.get(activation_token = activation_token)
    except User.DoesNotExist:
        return HttpResponse("El token de activación no es válido.")
    
    users.is_active = True
    users.save()
    
    success(request, message="Su cuenta a sido activada.")
    return redirect('signin')

def signup(request):
    form = MySocialUserCreationForm
    if request.method == "GET":
        
        return render(request, 'signup&login/signup.html', {"form":form})

    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            try:
                user_activate = form.save(commit=False)
                user_activate.activation_token = default_token_generator.make_token(user_activate)
                user_activate.save()
            except User.DoesNotExist:
                error(request, message='El usuario ya existe.')

            activation_link = f"http://127.0.0.1:8000/activate/{user_activate.activation_token}/"

            email_activation = email_service.EmailSevice()
            
            email_activation.send_email(
                to = user_activate.email,
                subject="¡Activar tu cuenta de Social NetWork!",
                html = f"""
                    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
                        <h2>Activación de Cuenta</h2>
                        <p>Hola {user_activate.username},</p>
                        <p>Gracias por registrarte en nuestro servicio. Para activar tu cuenta, por favor utiliza el siguiente enlace:</p>
                        <p style="background-color: #f0f0f0; padding: 10px; font-weight: bold; font-size: 18px;">{activation_link}</p>
                        <p>Una vez que hayas ingresado el código de activación, tu cuenta estará lista para usar.</p>
                        <p>Si no realizaste esta solicitud, por favor ignora este mensaje.</p>
                        <p>¡Gracias!</p>
                        <p>El equipo de Social Network</p>
                    </div>
                """
            )

            success(request, message="El usuario a sido creado")
            print(request.POST)
            # return redirect("activation")
            return render(request, 'signup&login/signup.html', {"form":form})
        else:
            error(request, message="Revisa los campos.")
        return render(request, 'signup&login/signup.html', {"form":form})

@login_required
def home(request):
    
    return render(request, "index.html", {})

def deleteuser(request):
    MySocialUser.objects.all().delete()
    return redirect("signup")
    