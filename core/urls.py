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
    path('post/<int:post_id>/', views.home, name='home_with_post'),
    path('siqnout/', views.siqnout, name='logout'),
    path('activate/<str:activation_token>/', views.activate_account, name='activate_account'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('friends/', views.friends, name='friends'),
    path('delete_friends/<int:id>',views.delete_friendship, name='delete_friends'),
    path('delete_posts/<int:id>', views.delete_post, name='delete_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('delete_user/', views.delete_user, name='delete_user')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
