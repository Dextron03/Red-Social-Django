from django.contrib import admin
from django.urls import path
from social_network import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('', views.home, name='home'),
    path('siqnout/', views.siqnout, name='siqnout'),
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('activate/<str:activation_token>/', views.activate_account, name='activate_account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
