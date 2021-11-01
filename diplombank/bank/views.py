from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .method import *
from .models import *


def read_or_load_data_db(request):
    query_courses_deposits = CoursesDepositsBank.objects.all()
    if query_courses_deposits.exists():
        read_courses_deposits_db()
    else:
        load_courses_deposits_in_db()
    return HttpResponse("")


class BankView(ListView):
    model = CoursesDepositsBank
    template_name = 'coursesdepositsbank_list.html'

    def get_queryset(self):
        date_now = date.today()
        return super().get_queryset().filter(date=date_now)
