from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
import urllib.request
import re
import sqlite3
import os
from bs4 import BeautifulSoup

from .models import GrantYears


def index(request):
    grants = GrantYears.objects.all()
    if not grants.exists():
        result = requests.get('https://ru.wikipedia.org/wiki/Университет_ИТМО').text
        result.encode("utf-8")
        row = ""
        soup = BeautifulSoup(result, 'lxml')
        sherlock = soup.find('dt', text="Гранты, бизнес-инкубаторы, коворкинги")
        sherlock1 = sherlock.find_parent("dl").find_next_siblings("p")
        for paragraph in sherlock1[:4]:
            year = re.search(r"\b\d{4}\b", paragraph.get_text()).group()
            desc = paragraph.get_text()
            desc = desc.replace("\n", "")
            desc = desc.replace("\xa0", " ")
            yr = GrantYears()
            yr.year = year
            yr.desc = desc
            yr.save()
    context = {
        'years': grants,
    }
    return render(request, 'index.html', context)


def addgrant(request):
    return render(request, 'addgrant.html')


def insert(request):
    if request.method == 'POST':
        form = GrantYears(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            desc = form.cleaned_data['desc']
            p = GrantYears(year=year, desc=desc)
            p.save()
