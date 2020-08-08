from django.shortcuts import render
from . models import info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_massege(requset):
    myinfo = info.objects.first()
    if requset.method =='POST':
        subject = requset.POST['subject']
        email = requset.POST['email']
        messge  = requset.POST['message']

        send_mail(subject,messge,email,[settings.EMAIL_HOST_USER])
    return render (requset , 'contact/contact.html' , {'myinfo':myinfo})