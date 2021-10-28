from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .method import get_courses, get_deposit_rate, save_courses_db, save_deposits_db
from .models import *


def load_base_view(request):
    courses = get_courses()
    deposits = get_deposit_rate()
    save_courses_db(courses, reset=True)
    save_deposits_db(deposits, reset=True)
    return HttpResponse("")


class AllCoursesView(ListView):
    model = CoursesBank
    template_name = 'coursebank_list.html'
