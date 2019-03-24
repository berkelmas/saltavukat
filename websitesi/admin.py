from django.contrib import admin
from .models import Makaleler, ContactForm, Randevular, Notlar

from django.contrib.auth.models import Group, User

# Register your models here.
class MakaleAdmin(admin.ModelAdmin):
    readonly_fields = ["makale_slug"]
admin.site.register(Makaleler, MakaleAdmin)

class ContactFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactForm, ContactFormAdmin)

class RandevularAdmin(admin.ModelAdmin):
    pass
admin.site.register(Randevular, RandevularAdmin)


class NotlarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notlar, NotlarAdmin)


admin.site.site_header = 'Salt Hukuk Yönetim Paneli'

admin.site.unregister(Group)
admin.site.unregister(User)