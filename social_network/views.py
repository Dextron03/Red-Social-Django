from django.shortcuts import render, redirect, get_object_or_404
from .forms import MySocialUserCreationForm, PostsForm, CommentForm
from .models import MySocialUser, Posts, Friends
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from dotenv import load_dotenv
from services.email_service import EmailService
from services.generate_password import GeneratePassword

load_dotenv("settings.py")

User = get_user_model()

def signin(request):    

    if request.method == "GET":
        
        return render(request, "signup&login/signin.html", {"form":AuthenticationForm})

    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        
        query_user_activate = MySocialUser.objects.filter(username = request.POST['username']).first()
        
        if query_user_activate is not None and query_user_activate.is_active is not True:
            messages.error(request, "El usuario no está activado.")
            return render(request, "signup&login/signin.html", {"form": AuthenticationForm})
          
        if user is None:
            messages.error(request, message="El usuario o la contraseña es incorrecta")
            return render(request, "signup&login/signin.html", {"form":AuthenticationForm})
        else:
            login(request, user)
            return redirect("home")

def siqnout(request):
    logout(request)
    return redirect("signin")

@login_required
def add_friend(request):
    if request.method == 'POST':
        friend_id = request.POST.get('friend_id')
        user = request.user
        friend = MySocialUser.objects.get(id=friend_id)
        
        if not Friends.objects.filter(user=user, friend=friend).exists():
            Friends.objects.create(user=user, friend=friend)
            messages.success(request, f'Solicitud de amistad enviada a {friend.name}')
        else:
            messages.error(request, f'Ya tienes una solicitud pendiente para {friend.name}')
        
        return redirect('home')


def activate_account(request, activation_token):
    try:
        users = User.objects.get(activation_token = activation_token)
    except User.DoesNotExist:
        return HttpResponse("El token de activación no es válido.")
    
    users.is_active = True
    users.save()
    
    messages.success(request, message="Su cuenta a sido activada.")
    return redirect('signin')

def signup(request):
    form = MySocialUserCreationForm()
    if request.method == "GET":
        
        return render(request, 'signup&login/signup.html', {"form": form})

    if request.method == "POST":
        form = MySocialUserCreationForm(request.POST, request.FILES) 
        # print(request.POST)
        if form.is_valid():
            try: 
                user_activate = form.save(commit=False)
                user_activate.activation_token = default_token_generator.make_token(user_activate)
                activation_link = f"http://127.0.0.1:8000/activate/{user_activate.activation_token}/"
                email_activation = EmailService()
                email_activation.send_email(
                    to=user_activate.email,
                    subject="¡Activar tu cuenta de Social NetWork!",
                    html=f"""
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
                user_activate.save()
            except User.DoesNotExist:
                error_message = 'El usuario ya existe.'
                messages.error(request, error_message)
            success_message = "El usuario ha sido creado, revise su correo electrónico para activar su cuenta."
            messages.success(request, success_message)
            return redirect('signin')
        else:
            error_message = "Revisa los campos."
            messages.error(request, error_message)
    return render(request, 'signup&login/signup.html', {"form": form})


def get_suggestions_from_friends(user_lg):
    friend = Friends.objects.filter(user=user_lg).values_list('friend', flat=True)
    
    suggestions = MySocialUser.objects.exclude(id__in=friend).exclude(id=user_lg.id)
    
    return suggestions

@login_required
def home(request, post_id=None):
    user_login = request.user
    query_posts = Posts.objects.all()
    
    suggestions = get_suggestions_from_friends(user_login)
    
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
            messages.success(request, 'Has agregado una nueva publicación')
            return redirect('home')  # Redirigir al usuario a la página de inicio después de agregar una publicación
        else:
            messages.error(request, 'Error al agregar la publicación. Por favor, revise los campos.')
    else:
        form_post = PostsForm() 
        form_comment = CommentForm()
    return render(request, "index.html", {"all_post": query_posts,
                                          'form_post': form_post,
                                          "form_comment":form_comment,
                                          'users': suggestions 
                                          })
@login_required
def friends(request):
    user_login = request.user
    friend_ids = user_login.friends.values_list('friend_id', flat=True)
    friend_posts = Posts.objects.filter(user_id__in=friend_ids).order_by('-date')
    
    friends_user = user_login.friends.values_list('friend_id', flat=True)
    friends_r = Friends.objects.filter(user_id__in=friends_user)
    
    return render(request, 'friends.html', {
        'friend_posts': friend_posts,
        'friends':friends_r
        })

@login_required
def delete_friendship(request, id):
    try:
        friendship = Friends.objects.get(id=id)
        friendship.delete()
        messages.success(request, message='Se a roto la amistad ')
        return redirect('friends')
    except User.DoesNotExist:
        messages.error(request, message='Esta amistad no se encuentra.')
        return redirect('friends')
 
@login_required   
def delete_post(request, id):
    post_select = Posts.objects.get(id=id)
    post_select.delete()    
    messages.success(request, message='Haz borrado la publicacion.')
    return redirect('home')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'La publicación se ha editado correctamente.')
            return redirect('home')
        else:
            messages.error(request, 'Algo ha salido mal con la edición de esta publicación.')
    else:
        form = PostsForm(instance=post)
    
    return render(request, 'form/edit_post.html', {'form': form, 'post_id': post_id})

def password_reset(request):
    if 'passwordReset' in request.GET:
        username = request.GET.get('passwordReset', "")
        user = get_object_or_404(MySocialUser, username__contains=username)  # Obtener el usuario o devolver un error 404 si no se encuentra

        if user.email:  # Verificar si el usuario tiene un correo electrónico asociado
            email_service = EmailService()
            generate_password = GeneratePassword()
            new_password = generate_password.generator()

            user.set_password(new_password)  # Establecer la nueva contraseña
            user.save()

            email_service.send_email(
                to=user.email,
                subject="Contraseña Restablecida",
                html=f"""
                    <div style="max-width: 600px; margin: 20px auto; background-color: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                        <div style="text-align: center; margin-bottom: 20px;">
                                <img src="../static/img/logo.png" alt="Logo de la Compañía" style="max-width: 150px; height: auto;">
                        </div>
                        <div style="padding: 20px;">
                            <p>¡Hola!</p>
                            <p>Recibiste este correo electrónico porque haz cambiado tu contraseña, la cual te hemos asignado:</p>
                            <p>{new_password}</p>
                            <p>Si no solicitaste restablecer tu contraseña, puedes ignorar este mensaje.</p>
                            <p>Gracias,<br>El equipo de Social NetWork</p>
                        </div>
                    </div>
                """
            )
            messages.success(request, message='Su contraseña ha sido cambiada. Por favor, revise su correo electrónico.')
            return redirect('signin')
        else:
            messages.error(request, message=f'El usuario {username} no tiene un correo electrónico asociado.')
            return redirect('signin')
    else:
        messages.error(request, message='El parámetro "passwordReset" no se proporcionó en la solicitud.')
        return redirect('signin')
        
def deleteuser(request):
    # MySocialUser.objects.all().delete()
    MySocialUser.objects.get(id=18).delete()
    return redirect("signup")
    