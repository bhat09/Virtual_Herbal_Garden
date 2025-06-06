"""
from  . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('index/', views.index,name='index'),
     path('herbs/', views.herbs,name='herbs'),
     path('add_herbs/', views.add_herbs,name='add_herbs'),
     path('about/', views.about,name='about'),
     path('find_remidy/', views.find_remidy,name='find_remidy'),
     path('herbs/', herb_list, name='herb_list'),
     path('contacts/', views.contacts,name='contacts'),
     path('contacts/submit/', views.contact_view, name='contact_submit'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('herbs/', views.herbs, name='herbs'),
    path('add_herbs/', views.add_herbs, name='add_herbs'),
    path('about/', views.about, name='about'),
    path('find_remidy/', views.find_remidy, name='find_remidy'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/submit/', views.contact_view, name='contact_submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
