from django.shortcuts import render, redirect, get_object_or_404
from .forms import MySocialUserCreationForm, PostsForm, CommentForm
from .models import MySocialUser, Posts
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
        
        
        query_user_activate = MySocialUser.objects.filter(username = request.POST['username']).first()
        
        if query_user_activate is not None and query_user_activate.is_active is not True:
            error(request, "El usuario no está activado.")
            return render(request, "signup&login/signin.html", {"form": AuthenticationForm})
          
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
        form = form(request.POST, request.FILES)
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

            success(request, message="El usuario a sido creado, revise su correo electronico para activar su usuario.")
            print(request.POST)
            # return redirect("activation")
            # return render(request, 'signup&login/signup.html', {"form":form})
            return redirect('signin')
        else:
            error(request, message="Revisa los campos.")
        return render(request, 'signup&login/signup.html', {"form":form})

@login_required
def home(request, post_id=None):
    user_login = request.user
    query_posts = Posts.objects.all()
    
    if post_id is not None:
        post = get_object_or_404(Posts, pk=post_id)  # Obtiene la instancia de la publicación basada en el ID proporcionado
    else:
        post = None
    
    if request.method == "POST":
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.user = user_login
            if post is not None:
                comment.posts = post  
            comment.save()
            return redirect("home")
        
        form_post = PostsForm(request.POST, request.FILES)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.user = user_login
            post.save()
            success(request, 'Has agregado una nueva publicación')
            return redirect('home')  # Redirigir al usuario a la página de inicio después de agregar una publicación
        else:
            error(request, 'Error al agregar la publicación. Por favor, revise los campos.')
    else:
        form_post = PostsForm() 
        form_comment = CommentForm()
    return render(request, "index.html", {"all_post": query_posts, 'form_post': form_post, "form_comment":form_comment})
def deleteuser(request):
    MySocialUser.objects.all().delete()
    return redirect("signup")
    