from django.core.management.base import BaseCommand
from django.utils.formats import localize
import datetime
import requests
from bs4 import BeautifulSoup

from applications.finder.models import Domain


class Command(BaseCommand):
    all_domain = []

    def extract_domain(self):
        resp = requests.post(url="https://domainbigdata.com/nj/2yTlQHiod9ZJe-gXgtJ_9A")
        y = BeautifulSoup(resp.content, "lxml")
        t = y.find("table", attrs={"class": "t1"})
        z = t.find("tbody")
        for k in z.findAll("tr"):
            for p in k.findAll("td")[0]:
                self.all_domain.append(p.text)

    def handle(self, *args, **kwargs):
        self.extract_domain()
        for domain in self.all_domain:
            domain = Domain.objects.create(
                domain=domain, created_at="2021-06-10")
            domain.save()
