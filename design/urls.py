# urls.py
from django.urls import path
from .views import *



urlpatterns = [

    path('dn/<int:design_id>', dn, name='dn'),
    path('ww/<int:design_id>', WW, name='WW'),
    path('sw/<int:design_id>', sw, name='sw'),
    path('cw/<int:design_id>', cw, name='cw'),
    path('ld/<int:design_id>', ld, name='ld'),
    path('ex/<int:design_id>', ex, name='ex'),
    path('getValue/',getValue, name='getValue'),
    path('setww/',setww, name='setww'),
    path('upload-design/',upload_design_view, name='upload_design_view'),
    path('',home_page, name='home_page'),
    path('designs/', design_list, name='design_list'),

]