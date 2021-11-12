from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', BankView.as_view(), name='all'),
    path('deposit/', CreateBankView.as_view(), name='new'),
    path('single/', ClientList.as_view(), name='single'),
    path('<slag>/profit/', ProfitView.as_view(), name='margin'),
]