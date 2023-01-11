from django import forms
from django.db import models
from django.db.models import fields
from . models import Gallerry,Caricature,Portrait,Graphic,Illustration

class GallerryForm(forms.ModelForm):
    class Meta():
        model=Gallerry
        fields='__all__'

class CaricatureForm(forms.ModelForm):
    class Meta():
        model=Caricature
        fields='__all__'

class PortraitForm(forms.ModelForm):
    class Meta():
        model=Portrait
        fields='__all__'

class GraphicForm(forms.ModelForm):
    class Meta():
        model=Graphic
        fields='__all__'

class IllustrationForm(forms.ModelForm):
    class Meta():
        model=Illustration
        fields='__all__'