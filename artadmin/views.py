from django.shortcuts import render,redirect
from artadmin.forms import GallerryForm,CaricatureForm,IllustrationForm,PortraitForm,GraphicForm
from artadmin.models import Gallerry,Caricature,Portrait,Illustration,Graphic,ContactUs
from django.http import HttpResponse  
from artgallerry import settings  
from django.core.mail import send_mail 


# Create your views here.
def adminindex(request):
    return render(request, 'adminindex.html')

def gallerry(request):
    if request.method=='POST':
        form=GallerryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            image=form.cleaned_data['Image']
            name=form.cleaned_data['Name']
            form.save()
    else:
        form=GallerryForm()
    return render(request,'gallerry.html',{'form':form})

def caricature(request):
    if request.method=='POST':
        form=CaricatureForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            image=form.cleaned_data['Caricature_Img']
            name=form.cleaned_data['Caricature_Name']
            form.save()
    else:
        form=CaricatureForm()
    return render(request,'admincaricature.html',{'form':form})
def viewcaricatures(request):
    data=Caricature.objects.all()
    return render(request, 'viewcaricatures.html',{'data':data})

def caricatureupdate(request,id):
    cari=Caricature.objects.get(id=id)
    if request.method=='POST':
        form=CaricatureForm(request.POST or None,request.FILES or None,instance=cari)
        if form.is_valid():
            image=form.cleaned_data['Caricature_Img']
            name=form.cleaned_data['Caricature_Name']
            form.save()
            return redirect("/artadmin/viewcaricatures")
    else:
        form=CaricatureForm(instance=cari)
    return render(request,'caricatureupdate.html',{'form':form,'cari':cari})

def caricaturedestroy(request, id):
    cari = Caricature.objects.get(id=id)
    cari.delete()
    return redirect("/viewcaricatures")





def portrait(request):
    if request.method=='POST':
        form=PortraitForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            image=form.cleaned_data['Portrait_Img']
            name=form.cleaned_data['Portrait_Name']
            form.save()
    else:
        form=PortraitForm()
    return render(request,'adminportrait.html',{'form':form})
def viewportraits(request):
    data=Portrait.objects.all()
    return render(request, 'viewportraits.html',{'data':data})

def portraitupdate(request,id):
    port=Portrait.objects.get(id=id)
    if request.method=='POST':
        form=PortraitForm(request.POST or None,request.FILES or None,instance=port)
        if form.is_valid():
            image=form.cleaned_data['Portrait_Img']
            name=form.cleaned_data['Portrait_Name']
            form.save()
            return redirect("/artadmin/viewportraits")
    else:
        form=PortraitForm(instance=port)
    return render(request,'portraitupdate.html',{'form':form,'port':port})

def portraitdestroy(request, id):
    port = Portrait.objects.get(id=id)
    port.delete()
    return redirect("/viewportraits")





def graphic(request):
    if request.method=='POST':
        form=GraphicForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            image=form.cleaned_data['Graphic_Img']
            name=form.cleaned_data['Graphic_Name']
            form.save()
    else:
        form=GraphicForm()
    return render(request,'admingraphic.html',{'form':form})

def viewgraphics(request):
    data=Graphic.objects.all()
    return render(request, 'viewgraphics.html',{'data':data})

def graphicupdate(request,id):
    grap=Graphic.objects.get(id=id)
    if request.method=='POST':
        form=GraphicForm(request.POST or None,request.FILES or None,instance=grap)
        if form.is_valid():
            image=form.cleaned_data['Graphic_Img']
            name=form.cleaned_data['Graphic_Name']
            form.save()
            return redirect("/artadmin/viewgraphics")
    else:
        form=GraphicForm(instance=grap)
    return render(request,'graphicupdate.html',{'form':form,'grap':grap})

def graphicdestroy(request, id):
    grap = Graphic.objects.get(id=id)
    grap.delete()
    return redirect("/viewgraphics")





def illustration(request):
    if request.method=='POST':
        form=IllustrationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            image=form.cleaned_data['Illustration_Img']
            name=form.cleaned_data['Illustration_Name']
            form.save()
    else:
        form=IllustrationForm()
    return render(request,'adminillustration.html',{'form':form})

def viewillustrations(request):
    data=Illustration.objects.all()
    return render(request, 'viewillustrations.html',{'data':data})

def illustrationupdate(request,id):
    grap=Illustration.objects.get(id=id)
    if request.method=='POST':
        form=IllustrationForm(request.POST or None,request.FILES or None,instance=grap)
        if form.is_valid():
            image=form.cleaned_data['Illustration_Img']
            name=form.cleaned_data['Illustration_Name']
            form.save()
            return redirect("/artadmin/viewillustrations")
    else:
        form=IllustrationForm(instance=grap)
    return render(request,'illustrationupdate.html',{'form':form,'grap':grap})

def illustrationdestroy(request, id):
    grap = Illustration.objects.get(id=id)
    grap.delete()
    return redirect("/viewillustrations")






# def contactus(request):
#     if request.method=='POST':
#         cname=request.POST.get('contact_name')
#         cemail=request.POST.get('contact_email')
#         cmessage=request.POST.get('contact_message')
#         tab=ContactUs(Contact_Name=cname,Contact_Email=cemail,Contact_Message=cmessage)
#         tab.save()
#         return redirect('/')
#     else:
#         return render(request, 'index.html')


# def mail(request):  
#     if request.method=='POST':
#         cname=request.POST.get('contact_name')
#         cemail=request.POST.get('contact_email')
#         cmessage=request.POST.get('contact_message')
#         res     = send_mail(cname, cmessage, settings.EMAIL_HOST_USER, [cemail],fail_silently=False)  
#         if(res == 1):  
#             msg = "Mail Sent Successfuly"  
#         else:  
#             msg = "Mail could not sent"  
#         return HttpResponse(msg)
#     else:
#         return render(request, 'index.html')



def viewcontactus(request):
    cont=ContactUs.objects.all()
    return render(request,'viewcontactus.html',{'cont':cont})

def contactdestroy(request, id):
    grap = ContactUs.objects.get(id=id)
    grap.delete()
    return redirect("/artadmin/viewcontactus")