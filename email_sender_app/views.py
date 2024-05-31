from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from form_submmission import fill_form
# Create your views here.


def send_email(request):
    form_link = 'https://forms.gle/WT68aV5UnPajeoSc8'
    fill_form(form_link)
    email = EmailMessage(
        'Python (Selenium) Assignment - Khaled Lotfy',
        'Please find here the attached screenshot of the confirmation page.',
        'klotfy785@gmail.com',
        ['lotfyk29@yahoo.com'],

    )
    email.attach_file('confirmation.png')
    email.send()

    return HttpResponse('Email sent successfully!')