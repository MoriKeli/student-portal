from django.urls import path
from students import views

urlpatterns = [
    path('', views.UserLogin.as_view(), name='login'),
    path('create-account/', views.create_account_view, name='signup'),
    path('homepage/welcome-to-sportal/', views.homepage_view, name='homepage'),
    path('student-profile/', views.student_profile_view, name='student_profile'),
    
    
    path('logout', views.LogoutUser.as_view(), name='logout'),
]