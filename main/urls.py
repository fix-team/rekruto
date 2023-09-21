from django.urls import path
from .views import HelloView

urlpatterns = [
    path('', HelloView, name='hello')
]
