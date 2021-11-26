from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', BankView.as_view(), name='all'),
    path('deposit/', CreateBankView.as_view(), name='new'),
    path('single/', ClientList.as_view(), name='single'),
    path('view/<slag>/profit/', ProfitView.as_view(), name='margin'),
    path('view/', deposit_queryset, name='deposit'),
]