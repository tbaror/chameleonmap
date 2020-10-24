from django.urls import path
from authentication.views import LoginUsers

from . import views

app_name = "auth"

urlpatterns = [
    path('login/', LoginUsers.as_view(), name="login")
]
