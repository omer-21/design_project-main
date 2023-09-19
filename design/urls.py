# urls.py
from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('dn/', dn, name='dn'),
    path('ww/', WW, name='WW'),
    path('sw/', sw, name='sw'),
    path('cw/', cw, name='cw'),
    path('ld/', ld, name='ld'),
    path('ex/', ex, name='ex'),
    path('getValue/',getValue, name='getValue'),
    path('setww/',setww, name='setww'),

    
]