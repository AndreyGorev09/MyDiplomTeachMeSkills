from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CoursesDepositsBank(models.Model):
    date = models.DateField(verbose_name='дата')
    usd = models.CharField(max_length=3, verbose_name='валюта')
    usd_buy = models.FloatField(verbose_name='курс покупки доллара')
    usd_sale = models.FloatField(verbose_name='курс продажи доллара')
    eur = models.CharField(max_length=3, verbose_name='валюта')
    eur_buy = models.FloatField(verbose_name='курс покупки евро')
    eur_sale = models.FloatField(verbose_name='курс продажи евро')
    rub = models.CharField(max_length=3, verbose_name='валюта')
    rub_buy = models.FloatField(verbose_name='курс покупки рос.рубли')
    rub_sale = models.FloatField(verbose_name='курс продажи рос.рубли')
    rate_byn = models.FloatField(verbose_name='ставка вклада BYN')
    rate_usd = models.FloatField(verbose_name='ставка вклада USD')
    rate_eur = models.FloatField(verbose_name='ставка вклада EUR')
    rate_rub = models.FloatField(verbose_name='ставка вклада RUB')


class Client(models.Model):
    deposit_sum = models.IntegerField(verbose_name='сумма вклада')
    period = models.IntegerField(verbose_name='период')
    client = models.ForeignKey(User, on_delete=models.CASCADE)
