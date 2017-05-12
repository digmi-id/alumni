from django.conf.urls import url
from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tentang/', views.about, name='about'),
    url(r'^kontak/', views.contact, name='contact'),
    url(r'^faq/', views.faq, name='faq'),
]
