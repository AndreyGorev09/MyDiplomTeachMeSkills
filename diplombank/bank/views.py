from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .method import *
from .models import *


class BankView(ListView):
    model = CoursesDepositsBank
    template_name = 'coursesdepositsbank_list.html'

    def get_queryset(self):
        date_now = date.today()
        read_or_load_courses_deposits_db()
        return super().get_queryset().filter(date=date_now)


class CreateBankView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['deposit_sum', 'period']
    success_url = reverse_lazy('diplherok:all')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.client_bank = self.request.user
        obj.save
        return super().form_valid(form)

