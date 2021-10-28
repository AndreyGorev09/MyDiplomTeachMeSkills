from django.urls import path
from .views import *


app_name = "bank"

urlpatterns = [
    path('', AllCoursesView.as_view(), name='all'),
]