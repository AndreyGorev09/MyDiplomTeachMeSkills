from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', read_or_load_data_db),
    path('bank/', AllCoursesView.as_view(), name='all'),
]