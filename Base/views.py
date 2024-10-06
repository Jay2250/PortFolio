from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
import re
import traceback
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
# from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.

def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')
        print(name, email, number, content)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(
                request, 'Lenght of name should be greater than 2 and less than 30 words ')
            return render(request, 'index.html')

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if len(email) > 1 and len(email) < 30 and re.fullmatch(regex, email):
            pass
        else:
            messages.error(request, 'invaild email try again ')
            return render(request, 'index.html')
        print(len(number))
        # if len(number) > 9 and len(number) <= 13:
        #     pass
        # else:
        #     messages.error(request, 'invaild number please try again ')
        #     return render(request, 'index.html')
        
        # try:
        #     print('Connecting to DB...')
        #     ins = models.Contact(name=name, email=email,
        #                      content=content, number=number)
        #     print('Connected to DB. Saving to DB')
        #     ins.save()
        #     print('Saved to DB')
        # except:
        #      traceback.print_exc()
        subject = f"New Contact from PortFolio, Form Submission from {name}"
        message_body = f"Name: {name}\nEmail: {email}\nMessage:\n{content}"
        recipient_list = ['jayeshchauriwar@gmail.com']
            
        try:
                print('Sending Mail')
                send_mail(subject, message_body, email, recipient_list)
                return HttpResponse(content="OK", status=200)
        except Exception as e:
                return HttpResponse(f"Failed to send email: {e}")
        
    return render(request, 'index.html')
    
    
    