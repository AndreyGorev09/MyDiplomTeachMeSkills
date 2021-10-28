from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', load_base_view),
    path('bank/', AllCoursesView.as_view(), name='all'),
]