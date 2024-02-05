from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage


def say_hello(request):
    try:
        EmailMessage('subject', 'message', 'ok@ok.com'['ok@2ok.com',])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
