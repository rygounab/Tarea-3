from django.urls import path
from patrones import views

urlpatterns = [
    path('', views.menu, name="menu"),
    path('mf', views.mf, name="mf"),
    path('cd', views.cd, name="cd"),
    path('ls', views.ls, name="ls"),
]
