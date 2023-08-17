from django.urls import path
from usr.views import Register

urlpatterns = [
    path('', Register.as_view(), name='register')
]