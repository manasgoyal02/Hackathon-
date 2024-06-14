from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.welcome_page, name='welcome'),
    path('', views.next_page, name='login'),
    path('', views.index, name='index'),
    path('', views.education, name='education'),
    path('', views.health, name='health'),
    path('', views.justice, name='justice'),
    path('', views.publicworks, name='pwd'),
    path('', views.laworder, name='law'),
    path('', views.revenue, name='revenue'),
]