from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from form_submmission import fill_form
from decouple import config
# Create your views here.


def send_email(request):
    form_link = 'https://forms.gle/WT68aV5UnPajeoSc8'
    fill_form(form_link)
    

    # Email data
    subject = 'Python (Selenium) Assignment - Your Name'
    body = 'Please find the screenshot attached.'
    from_email = config('EMAIL_ADDRESS')
    to_email = ['tech@themedius.ai']
    cc_email = ['HR@themedius.ai']

    email = EmailMessage(subject, body, from_email, to_email, cc=cc_email)
    email.attach_file('confirmation.png')
    email.send()

    return HttpResponse('Email sent successfully!')