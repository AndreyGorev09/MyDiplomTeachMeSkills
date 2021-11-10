from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', BankView.as_view(), name='all'),
    path('deposit/', CreateBankView.as_view(), name='new'),
    path('profit/', ProfitView.as_view(), name='margin'),
]