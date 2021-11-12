from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Client(models.Model):
    deposit_sum = models.IntegerField(verbose_name='deposit amount')
    period = models.IntegerField(verbose_name='period in days',
                                 validators=[MinValueValidator(1), MaxValueValidator(360)],
                                 )
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/{self.client}/profit"


class CoursesDepositsBank(models.Model):
    date = models.DateField(verbose_name='date')
    usd = models.CharField(max_length=3, verbose_name='currency')
    usd_buy = models.FloatField(verbose_name='dollar purchase rate')
    usd_sale = models.FloatField(verbose_name='dollar selling rate')
    eur = models.CharField(max_length=3, verbose_name='currency')
    eur_buy = models.FloatField(verbose_name='euro purchase rate')
    eur_sale = models.FloatField(verbose_name='euro selling rate')
    rub = models.CharField(max_length=3, verbose_name='currency')
    rub_buy = models.FloatField(verbose_name='purchase rate RUB')
    rub_sale = models.FloatField(verbose_name='sale rate RUB')
    rate_byn = models.FloatField(verbose_name='deposit rate BYN')
    rate_usd = models.FloatField(verbose_name='deposit rate USD')
    rate_eur = models.FloatField(verbose_name='deposit rate EUR')
    rate_rub = models.FloatField(verbose_name='deposit rate RUB')

    def get_absolute_url(self):
        return f"/{self.pk}/"


class ProfitDepositsClient(models.Model):
    date = models.DateField(verbose_name='date')
    profit_usd = models.FloatField(verbose_name='income at the deposit rate of USD')
    profit_eur = models.FloatField(verbose_name='income at the deposit rate of EUR')
    profit_rub = models.FloatField(verbose_name='income at the deposit rate of RUB')
    profit_byn = models.FloatField(verbose_name='income at the deposit rate of BYN')
    contributor = models.ForeignKey(Client, on_delete=models.CASCADE)


