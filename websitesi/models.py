from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class Notlar(models.Model):
    not_isim = models.CharField(('Not Bırakanın İsmi'), max_length=150)
    not_mail = models.CharField(('Not Bırakanın Maili'), max_length=100)
    not_mesaj = models.TextField('Not Bırakanın Mesajı')
    not_tarih = models.DateTimeField(('Not Bırakılma Tarihi') ,auto_now_add=True)

    def __str__(self):
        return self.not_isim

    class Meta:
        ordering= ("-not_tarih",)
        verbose_name = "Not"
        verbose_name_plural = "Notlar"

class Randevular(models.Model):
    randevu_isim = models.CharField(max_length= 100)
    randevu_ulasim = models.CharField(('İletişim Adresi'), max_length= 100)
    randevu_tarih = models.CharField(('Talep Edilen Randevu Tarihi'), max_length=100)
    randevu_saat = models.CharField(('Talep Edilen Randevu Saati'), max_length=100)
    randevu_mesaj = models.TextField(('Mesaj'))

    def __str__(self):
        return self.randevu_isim

    class Meta:
        ordering= ("-randevu_tarih",)
        verbose_name = "Randevu"
        verbose_name_plural = "Randevular"

class ContactForm(models.Model):
    iletisim_isim = models.CharField(('İletişim Talep Edenin Adı') ,max_length=100)
    iletisim_konu = models.CharField(('İletişim Talebinin Konusu'), max_length=100)
    iletisim_ulasim = models.CharField(('Ulaşım Adresi'), max_length=100)
    iletisim_mesaj = models.TextField(('Mesaj'))

    iletisim_tarih = models.DateField('Mesaj Tarihi', auto_now_add=True)

    def __str__(self):
        return self.iletisim_isim

    class Meta:
        ordering = ('-iletisim_tarih',)
        verbose_name = "İletişim Talebi"
        verbose_name_plural = "İletişim Talepleri"

class Makaleler(models.Model):
    makale_baslik = models.CharField(('Makale Başlığı'), max_length=150)
    makale_yayintarihi = models.DateField(('Makale Yayın Tarihi'))
    makale_mesaj = RichTextField()
    makale_slug = models.SlugField(unique=True, default='')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.makale_baslik

    def save(self, *args, **kwargs):
        self.makale_slug = slugify(self.makale_baslik)
        super(Makaleler, self).save(*args, **kwargs)

    class Meta:
        ordering= ('-makale_yayintarihi',)
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"
