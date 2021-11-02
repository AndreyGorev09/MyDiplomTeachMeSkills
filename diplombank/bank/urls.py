from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', BankView.as_view(), name='all'),
]