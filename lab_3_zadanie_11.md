from Osoby.models import Osoba 
Osoba.objects.all()

Osoba.objects.filter(id=3)

Osoba.objects.filter(imie__startswith="P") 

Osoba.objects.all().distinct('druzyna')

Osoba.objects.all().order_by('-druzyna')

Osoba.objects.create(imie="Bruce", nazwisko="Springsteen")