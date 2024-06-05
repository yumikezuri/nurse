from django.urls import path
from .views import HomeView

app_name = 'calculate'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]