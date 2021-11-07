from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Client(models.Model, IntegerRangeField):
    deposit_sum = models.IntegerField(verbose_name='сумма вклада')
    period = IntegerRangeField(verbose_name='период', min_value=1, max_value=360)
    client = models.ForeignKey(User, on_delete=models.CASCADE)


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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)




