from django.urls import path
from .views import HomeView, BPView

app_name = 'calculate'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('bp/', BPView.as_view(), name='bp'),
]