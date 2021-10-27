import decimal
from decimal import Decimal
import django.utils.timezone
import requests
from bs4 import BeautifulSoup
from .models import CoursesBank, DepositBank

depo_url = 'https://bankdabrabyt.by/personal/deposite/vklad-na-maru/'
kur_url = 'https://bankdabrabyt.by/export_courses.php'

# -------------------------------------- "Функция парсинга курса валют" -------------------------------------
def pars(url: str) -> 'bs4.element.Tag':
    url_pars = requests.get(url)
    url_body = url_pars.content.decode()
    soup = BeautifulSoup(url_body)
    return soup


def get_courses():
    result = []
    currency_body = pars(kur_url)
    data = django.utils.timezone.now()
    raw_usd = currency_body.find(code='840')
    usd = raw_usd.get('iso')
    usd_buy = Decimal(raw_usd.get('buy')).quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
    usd_sale = Decimal(raw_usd.get('sale')).quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
    raw_eur = currency_body.find(code='978')
    eur = raw_eur.get('iso')
    eur_buy = Decimal(raw_eur.get('buy')).quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
    eur_sale = Decimal(raw_eur.get('sale')).quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
    raw_rub = currency_body.find(code='643')
    rub = raw_rub.get('iso')
    rub_buy_float = float(raw_rub.get('buy')) * 100
    rub_buy = Decimal(rub_buy_float).quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
    rub_sale_float = float(raw_rub.get('sale')) * 100
    rub_sale = Decimal(rub_sale_float).quantize(Decimal('.01'), rounding=decimal.ROUND_DOWN)
    result.append(CoursesBank(
        data=data,
        usd=usd,
        usd_buy=usd_buy,
        usd_sale=usd_sale,
        eur=eur,
        eur_buy=eur_buy,
        eur_sale=eur_sale,
        rub=rub,
        rub_buy=rub_buy,
        rub_sale=rub_sale)
    )
    return result


def get_deposit_rate():
    result = []
    depo_body = pars(depo_url)

    data = django.utils.timezone.now()

    list_rate_byn = list(depo_body.find_all(name='b'))[4]
    row_rate_byn = str(list_rate_byn)
    rate_byn = row_rate_byn.strip('<b/%>').replace(',', '.')

    list_rate_usd = list(depo_body.find_all(name='b'))[6]
    row_rate_usd = str(list_rate_usd)
    rate_usd = row_rate_usd.strip('<b/%>').replace(',', '.')

    list_rate_eur = list(depo_body.find_all(name='b'))[7]
    row_rate_eur = str(list_rate_eur)
    rate_eur = row_rate_eur.strip('<b/%>').replace(',', '.')

    list_rate_rub = list(depo_body.find_all(name='b'))[8]
    row_rate_rub = str(list_rate_rub)
    rate_rub = row_rate_rub.strip('<b/%>').replace(',', '.')
    result.append(DepositBank(
        data=data,
        rate_byn=float(rate_byn),
        rate_usd=float(rate_usd),
        rate_eur=float(rate_eur),
        rate_rub=float(rate_rub)
    ))
    return result


def get_existing_courses():
    query = CoursesBank.objects.all()
    return [row.data for row in query]


def get_existing_deposits():
    query = DepositBank.objects.all()
    return [row.data for row in query]


def save_courses_db(courses, reset=False):
    if not reset:
        for course in courses:
            if course.data in get_existing_courses():
                continue
            course.save()
    else:
        CoursesBank.objects.all().delete()
        for course in courses:
            course.save()


def save_deposits_db(deposits, reset=False):
    if not reset:
        for rate in deposits:
            if rate.data in get_existing_deposits():
                continue
            rate.save()
    else:
        DepositBank.objects.all().delete()
        for rate in deposits:
            rate.save()
