from django.shortcuts import render
from django.contrib import messages
from .models import Randevular, Notlar, ContactForm, Makaleler
from django.core.paginator import Paginator

from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import requests

# Create your views here.
def index(request):
    if 'randevual' in request.POST:

        ## Bunlar randevu mesajları için
        isim = request.POST.get('isim')
        ulasim = request.POST.get('ulasim')
        tarih= request.POST.get('tarih')
        zaman = request.POST.get('zaman')
        mesaj = request.POST.get('mesaj')

        subject = 'Randevu Talebi'
        message = mesaj + "\n Ulaşım Bilgisi: " + ulasim + "\n Ad-Soyad: " + isim + "\nGönderi Tarihi: " + tarih
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['berkelmas96@gmail.com']
        send_mail(subject, message, email_from, recipient_list)

        randevu = Randevular(randevu_isim= isim, randevu_mesaj= mesaj, randevu_tarih= tarih, randevu_saat=zaman, randevu_ulasim=ulasim)
        randevu.save()

        return render(request, 'websitesi/index.html', {'nbar': 'index'})

    if 'notbirak' in request.POST:
        ## Bunlar Bırakılan Notlar İçin
        notisim = request.POST.get('notisim')
        notmail = request.POST.get('notmail')
        notmesaj = request.POST.get('notmesaj')

        subject = "salthukuk.com Not Bırakıldı"
        message = notmesaj + "\n Ulaşım Bilgisi: " + notmail + "\n Ad-Soyad: " + notisim
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['berkelmas96@gmail.com']
        send_mail(subject, message, email_from, recipient_list)

        not1 = Notlar(not_isim=notisim, not_mail=notmail, not_mesaj=notmesaj)
        not1.save()

        return render(request, 'websitesi/index.html', {'nbar' : 'index'})

    sonmakaleler = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    return render(request, 'websitesi/index.html', {'nbar' : 'index', 'sonmakaleler' : sonmakaleler})

def about(request):
    return render(request, 'websitesi/about.html', {'nbar' : 'about'})

def practices(request):
    return render(request, 'websitesi/practices.html', {'nbar' : 'practices'})

def practices2(request):
    return render(request, 'websitesi/practices2.html', {'nbar' : 'practices'})

def avukatlar(request):
    return render(request, 'websitesi/avukatlar.html', {'nbar' : 'avukatlar'})

def contact(request):
    if request.method == 'POST':
        isim = request.POST.get('isim')
        soyisim = request.POST.get('soyisim')
        konu = request.POST.get('konu')
        ulasim = request.POST.get('ulasim')
        mesaj = request.POST.get('mesaj')

        iletisim = ContactForm(iletisim_isim= isim + " " + soyisim, iletisim_konu= konu, iletisim_mesaj=mesaj, iletisim_ulasim=ulasim)
        iletisim.save()

        response = requests.get('https://api.netgsm.com.tr/sms/send/get/?usercode=5073978264&password=berk693693693&gsmno=5073978264&message=' + 'İletişim Talebinde Bulunan: \n' + isim + ' ' + soyisim + '\n' +'Mesajı: \n' + mesaj + '\n' +'Ulaşım Adresi: \n' + ulasim + '&msgheader=08508408276&dil=TR')


        subject = "İletişim Formu Geldi"
        message = mesaj + "\n <h1>Ulaşım Bilgisi:</h1> " + ulasim + "\n Ad-Soyad: " + isim + " " + soyisim
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['berkelmas96@gmail.com']


        html_content = render_to_string('websitesi/mail.html', {'isim': isim + soyisim, 'mesaj' : mesaj, 'ulasim' : ulasim, 'konu' : konu})  # render with dynamic value
        plain_message = strip_tags(html_content)

        send_mail(subject, plain_message, email_from, recipient_list, html_message=html_content)

        messages.success(request, 'Mesajınız Başarı İle İletildi')
        return render(request, 'websitesi/contact.html', {'nbar': 'contact'})
    return render(request, 'websitesi/contact.html', {'nbar' : 'contact'})

def makaleler(request):

    makale_list = Makaleler.objects.all()   ## sonra bi sn kapı caldı geliyom
    paginator = Paginator(makale_list, 6)  # Her Sayfada 1 Makale Gösterilecek.

    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'websitesi/makaleler.html', {'nbar' : 'makaleler', 'articles' : articles})

def makale_detay(request, makaleslug):
    makale = Makaleler.objects.get(makale_slug=makaleslug)
    return render(request, 'websitesi/makaledetay.html', {'makale' : makale})


def mail(request):
    return render(request, 'websitesi/mail.html')