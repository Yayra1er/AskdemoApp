from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse

from .forms import DemandeDemoForm
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactUsForm
import logging
from django.urls import reverse
logger = logging.getLogger(__name__)
def home(request):
    return render(request, 'home.html')


def apropos(request):
    return render(request, 'apropos.html')


def solution(request):
    return  render(request, 'solution.html')


def offre(request):
    return render(request, 'offre.html')


def contact(request):
    if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            body = f"""
                Contacter pour suggestion ou inquiétude:
                Nom: {name}
                Email : {email}
                Subject: {subject}
                Message: {message}
                """
            # Création de l'e-mail
            email_message = EmailMessage(
                subject,
                body,
                email,
                ['passmyall@gmail.com']
            )
            try:
                email_message.send()
                messages.success(request, 'Votre message a été envoyé avec succès!')
                return redirect(reverse('success') + f'?email={email}&subject={subject}')
            except Exception as e:
                messages.error(request, f"Erreur lors de l'envoi de l'email: {e}")
                return render(request, 'contact.html')

    return render(request, 'contact.html')

def success_view(request):
    return render(request, 'success.html')