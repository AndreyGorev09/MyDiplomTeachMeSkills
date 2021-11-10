from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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
    success_url = reverse_lazy('diplherok:margin')

    def form_valid(self, form):
        query = Client.objects.all()
        query.delete()
        obj = form.save(commit=False)
        obj.client_bank = self.request.user
        obj.save()
        return super().form_valid(form)


class ProfitView(ListView):
    model = ProfitDepositsClient
    template_name = 'profitdepositsclient_list.html'

    def get_queryset(self):
        load_profit_deposits_in_db()
        return super().get_queryset().all()


