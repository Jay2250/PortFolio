from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
import re
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
# from django.contrib.auth.decorators import login_required

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
        if len(number) > 9 and len(number) < 13 and carrier._is_mobile(number_type(phonenumbers.parse(number))):
            pass
        else:
            messages.error(request, 'invaild number please try again ')
            return render(request, 'index.html')
        ins = models.Contact(name=name, email=email,
                             content=content, number=number)
        ins.save()
        messages.success(
            request, 'Thank You for contacting me!! Your message has been saved ')
        print('data has been saved to database')

        print('The request is no pass ')
    return render(request, 'index.html')
    
    
    