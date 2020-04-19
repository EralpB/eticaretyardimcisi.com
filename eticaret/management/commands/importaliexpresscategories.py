from django.core.management.base import BaseCommand
from eticaret.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):

        INPUT = ["Düğün ve Etkinlikler,5%","Güvenlik ve Koruma,5%","Telefon ve Telekomünikasyon,8%","Giyim Aksesuarları,8%","Ev Aletleri,5%","Mobilya,5%","Cep Telefonu Aksesuarları,5%","Otomobil ve Motosiklet,8%","Bilgisayar ve Ofis,5%","Anne ve Çocuk,8%","Elektronik Bileşenler ve Sarf Malzemeleri,8%","Spor ve Eğlence,8%","İç Çamaşırı,5%","Ev ve Bahçe,5%","Oyunlar,5%","Ofis ve Okul Malzemeleri,8%","Moda Aksesuarları,8%","Özel Kategori ( Gıda),8%","Kol Saati,8%"]

        website, _ = Website.objects.get_or_create(name='Aliexpress')
        imported_count = 0
        for line in INPUT:
            # line = "Düğün ve Etkinlikler,5%"
            line = line[:-1]
            # line = "Düğün ve Etkinlikler,5"
            category_name, category_percentage = line.split(',')
            # "Düğün ve Etkinlikler"      "5"

            Category.objects.get_or_create(
                website=website,
                name=category_name,
                defaults={'commission': float(category_percentage)}
            )
            imported_count += 1

        print('{} imported'.format(imported_count))
