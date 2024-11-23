from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.homepage, name='homepage'),  # maps the homepage view 
    path('register', views.register, name='register'), #maps to the registration form
    path('login', CustomLoginView.as_view(), name='login'), #maps to the login page
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'), #maps to logout view
    path('dashboard', views.dashboard, name='dashboard'), #maps to the dashboard
    path('book-session/', views.book_session, name='book_session'),
    path('counselors/', views.counselor_list, name='counselor_list'),
]
