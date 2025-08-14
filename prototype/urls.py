# prototype/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This path is for the main index page, which will be loaded when you visit the root URL.
    path('', views.index, name='index'),
    
    # This path is for the API endpoint that your frontend will call.
    path('generate-diagram/', views.generate_diagram, name='generate_diagram'),
    
    # This path is for the login page.
    path('login/', views.login_view, name='login'),

    # This path is for the logout view.
    path('logout/', views.logout_view, name='logout'),
]