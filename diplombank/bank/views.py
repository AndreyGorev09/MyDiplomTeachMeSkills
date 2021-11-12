from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
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


class ClientList(ListView):
    model = Client
    fields = ['deposit_sum', 'period']


class ProfitView(ListView):
    model = ProfitDepositsClient
    template_name = 'profitdepositsclient_list.html'

    def get_queryset(self):
        query_client = Client.objects.filter(client=self.request.user).order_by('-id')
        data_profit = profit_deposits_client()
        for obj in data_profit:
            for i in query_client:
                if i.client == self.request.user:
                    query_profit = ProfitDepositsClient.objects.filter(contributor=i.id)
                    if query_profit.exists():
                        a = [j.contributor for j in query_profit]
                        for f in query_profit:
                            if f.contributor in a:
                                return super().get_queryset().filter(contributor=i.id)
                    else:
                        obj.save()
                        return super().get_queryset().filter(contributor=i.id)
                else:
                    return None


class CreateBankView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['deposit_sum', 'period']
    success_url = reverse_lazy('bank:single')

    def form_valid(self, form):
        query_client = Client.objects.filter(client=self.request.user).order_by("-id")
        if query_client.exists():
            for i in query_client:
                if i.client == self.request.user:
                    query_delete = query_client.filter(client=self.request.user)
                    query_delete.delete()
                    obj = form.save(commit=False)
                    obj.client = self.request.user
                    obj.save()
                    return super().form_valid(form)
                else:
                    return None
        else:
            obj = form.save(commit=False)
            obj.client = self.request.user
            obj.save()
            return super().form_valid(form)