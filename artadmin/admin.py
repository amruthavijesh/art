from django.contrib import admin

from artadmin.models import Gallerry,Caricature,Portrait,Graphic,Illustration,ContactUs

# Register your models here.
admin.site.register(Gallerry)
admin.site.register(Caricature)
admin.site.register(Portrait)
admin.site.register(Graphic)
admin.site.register(Illustration)
admin.site.register(ContactUs)