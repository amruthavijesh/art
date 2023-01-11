from django.db import models

# Create your models here.
class Gallerry(models.Model):
    Image=models.ImageField(upload_to='gallerry/',blank=True,null=True)
    Name=models.CharField(max_length=20)
class Caricature(models.Model):
    Caricature_Img=models.ImageField(upload_to='caricature/',blank=True,null=True)
    Caricature_Name=models.CharField(max_length=20)
class Portrait(models.Model):
    Portrait_Img=models.ImageField(upload_to='portrait/',blank=True,null=True)
    Portrait_Name=models.CharField(max_length=20)
class Graphic(models.Model):
    Graphic_Img=models.ImageField(upload_to='graphic/',blank=True,null=True)
    Graphic_Name=models.CharField(max_length=20)
class Illustration(models.Model):
    Illustration_Img=models.ImageField(upload_to='illustration/',blank=True,null=True)
    Illustration_Name=models.CharField(max_length=20)

class ContactUs(models.Model):
    Contact_Name=models.CharField(max_length=20,default='')
    Contact_Email=models.EmailField(default='')
    Contact_Message=(models.CharField(max_length=200,default=''))