from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .method import *
from .models import *


def read_or_load_data_db(request):
    query_courses = CoursesBank.objects.all()
    query_deposits = DepositBank.objects.all()
    if query_courses.exists() and query_deposits.exists():
        read_courses_db()
        read_deposits_db()
    load_courses_in_db()
    load_deposits_in_db()
    return HttpResponse("")


class AllCoursesView(ListView):
    model = CoursesBank
    template_name = 'coursebank_list.html'

    def get_queryset(self):
        date_now = date.today()
        return super().get_queryset().filter(data=date_now)
