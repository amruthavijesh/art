from django.shortcuts import render
from artadmin.models import Caricature,Portrait,Graphic,Illustration
from django.http import HttpResponse  
from artgallerry import settings  
from django.core.mail import send_mail 
# Create your views here.
def index(request):
    data1=Caricature.objects.all()
    data2=Portrait.objects.all()
    data3=Graphic.objects.all()
    data4=Illustration.objects.all()
    return render(request, 'index.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4})

def caricature(request):
    data=Caricature.objects.all()
    return render(request, 'caricature.html',{'data':data})

def portrait(request):
    return render(request, 'portrait.html')

def graphic(request):
    return render(request, 'graphic.html')

def illustration(request):
    return render(request, 'illustration.html')




def mail(request):  
    if request.method=='POST':
        cname=request.POST.get('contact_name')
        cemail=request.POST.get('contact_email')
        cmessage=request.POST.get('contact_message')
        toemail="amruthavijesh91jun@gmail.com"
        res     = send_mail(cname, cmessage, settings.EMAIL_HOST_USER, [toemail],fail_silently=False)  
        if(res == 1):  
            msg = "Mail Sent Successfuly"  
        else:  
            msg = "Mail could not sent"  
        return HttpResponse(msg)
    else:
        return render(request, 'index.html')