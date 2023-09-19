# urls.py
from django.urls import path
from .views import *



urlpatterns = [

    path('dn/', dn, name='dn'),
    path('ww/', WW, name='WW'),
    path('sw/', sw, name='sw'),
    path('cw/', cw, name='cw'),
    path('ld/', ld, name='ld'),
    path('ex/', ex, name='ex'),
    path('getValue/',getValue, name='getValue'),
    path('setww/',setww, name='setww'),
    path('upload-design/',upload_design_view, name='upload_design_view'),
    path('',home_page, name='home_page'),
    path('',home_page, name='home_page'),
    path('designs/', design_list, name='design_list'),

]