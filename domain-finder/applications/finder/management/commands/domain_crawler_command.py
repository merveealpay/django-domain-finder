from django.core.management.base import BaseCommand
from django.utils.formats import localize
import datetime
import requests
from bs4 import BeautifulSoup

from applications.finder.models import Domain


class Command(BaseCommand):

    #TODO: isimlendirmeyi duzelt.

    def extract_domain(self):
        all_domain = []
        resp = requests.post(url="https://domainbigdata.com/nj/2yTlQHiod9ZJe-gXgtJ_9A")
        #TODO: istek hatalı olursa nasıl hareket edicez bunu kontrol et
        # y burda beatufilsoup object gibi de
        y = BeautifulSoup(resp.content, "lxml")
        # t yerine findtable fln de
        t = y.find("table", attrs={"class": "t1"})
        z = t.find("tbody")
        #bu forlardan bi yerinde patlarsa bu domain objeleri nereye gitcek, loglaman lazım
        #try exceptleri iyi kullan
        for k in z.findAll("tr"):
            for p in k.findAll("td")[0]:
               #Domain.objects.create(domain=p.text,  created_at="2021-07-15")
               all_domain.append(Domain.objects.create(domain=p.text, created_at="2021-07-15"))
               Domain.objects.bulk_create(all_domain)

    #aslında listeye ihtiyacın yok saveleme işlemini üst foınksiyonda yapabilrisin
    #def handle(self, *args, **kwargs):
        #new_all_domain = self.extract_domain()
        #elf.extract_domain()
        #or domain in self.all_domain:
        # for domain in new_all_domain:
        #     domain = Domain.objects.create(
        #         domain=domain, created_at="2021-07-15")
           #domain.save()
