from django.urls import path
from patrones import views

urlpatterns = [
    path('menu', views.menu, name="menu"),
    path('mf', views.mf, name="mf"),
]
