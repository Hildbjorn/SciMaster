from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user_agreement', UserАgreementView.as_view(), name='user_agreement'),
]
