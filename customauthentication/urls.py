from django.urls import path
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('lagout/', LogoutView.as_view(), name='logout'),
]