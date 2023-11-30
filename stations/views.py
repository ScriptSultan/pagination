import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


lst_read = []
with open('data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
    read = csv.DictReader(f)
    for row in read:
        lst_read.append(row)

def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    pagi = Paginator(lst_read, 10)
    lala = pagi.get_page(page_num)
    context = {
        'bus_stations': lala,
        'page': lala,
    }
    return render(request, 'stations/index.html', context)
