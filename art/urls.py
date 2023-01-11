from django.urls import path
from art import views
app_name='art'
urlpatterns=[
    path('',views.index,name='index'),
    path('caricature',views.caricature,name='caricature'),
    path('portrait',views.portrait,name='portrait'),
    path('graphic',views.graphic,name='graphic'),
    path('illustration',views.illustration,name='illustration'),
    path('mail',views.mail,name='mail'),
]