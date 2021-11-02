from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .method import *
from .models import *


class BankView(ListView):
    model = CoursesDepositsBank
    template_name = 'coursesdepositsbank_list.html'

    def get_queryset(self):
        date_now = date.today()
        read_or_load_data_db()
        return super().get_queryset().filter(date=date_now)
