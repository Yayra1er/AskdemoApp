from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apropos/', views.apropos, name='apropos'),
    path('solution/', views.solution, name='solution'),
    path('offre/', views.offre, name='offre'),
    path('contact/', views.contact, name='contact'),
]