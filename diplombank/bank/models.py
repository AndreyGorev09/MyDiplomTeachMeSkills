from django.db import models


class CoursesBank(models.Model):
    data = models.DateField(verbose_name='дата', auto_now=True)
    usd = models.CharField(max_length=3, verbose_name='валюта')
    usd_buy = models.FloatField(verbose_name='курс покупки доллара')
    usd_sale = models.FloatField(verbose_name='курс продажи доллара')
    eur = models.CharField(max_length=3, verbose_name='валюта')
    eur_buy = models.FloatField(verbose_name='курс покупки евро')
    eur_sale = models.FloatField(verbose_name='курс продажи евро')
    rub = models.CharField(max_length=3, verbose_name='валюта')
    rub_buy = models.FloatField(verbose_name='курс покупки рос.рубли')
    rub_sale = models.FloatField(verbose_name='курс продажи рос.рубли')


class DepositBank(models.Model):
    data = models.DateField(verbose_name='дата', auto_now=True)
    rate_byn = models.FloatField(verbose_name='ставка вклада BYN')
    rate_usd = models.FloatField(verbose_name='ставка вклада USD')
    rate_eur = models.FloatField(verbose_name='ставка вклада EUR')
    rate_rub = models.FloatField(verbose_name='ставка вклада RUB')


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    password = models.CharField(max_length=150, verbose_name='пароль')
    deposit_sum = models.IntegerField(verbose_name='сумма вклада')
    period = models.IntegerField(verbose_name='период')
    deposit = models.ForeignKey(DepositBank, on_delete=models.CASCADE)
