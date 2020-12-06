from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('signup', views.SignUpView.as_view()),
]