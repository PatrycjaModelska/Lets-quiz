from django.urls import path, include
from django.contrib.auth  import views as auth_views
from . import views

urlpatterns = [
    
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/', views.SignUpView, name='signup'),
    path('profil/', views.profile, name='profile'),
    path('edit_photo/', views.edit_photo, name='edit_photo'),
]
