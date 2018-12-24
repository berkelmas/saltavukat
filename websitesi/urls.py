from django.urls import path
from .views import index, about, practices, practices2, avukatlar, contact, makaleler, makale_detay, mail

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('practices/', practices, name="practices"),
    path('practices2/', practices2, name="practices2"),
    path('avukatlar/', avukatlar, name="avukatlar"),
    path('contact/', contact, name="contact"),
    path('makaleler/', makaleler, name="articles"),
    path('makale/<slug:makaleslug>', makale_detay, name="makaledetay"),
    path('mail/', mail, name="mail"),
]
