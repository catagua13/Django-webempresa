from django.urls import path
from agendar import views
urlpatterns = [
    path('agendar', views.agendar, name="agendar")

]