from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('view_result/<str:audit_id>/', views.view_result, name='view_result'),
]
