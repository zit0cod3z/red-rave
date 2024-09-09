from django.shortcuts import render, redirect
from django.http import HttpResponse
from heirs_holding_app.models import Registration
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import *

# Create your views here.
def register(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		phone_number = request.POST.get("phone_number")
		instance = Registration(name=name, email=email, phone_number=phone_number)
		instance.save()

		my_subject = "HEIRS HOLDING PARTY CONFIRMATION"
		my_recipient = email
		mailer = settings.EMAIL_HOST_USER
		welcome_message = name

		html_message = render_to_string("heirs_holding_app/email.html")
		plain_message = strip_tags(html_message)

		message = EmailMultiAlternatives(
			subject = my_subject,
			body = plain_message,
			from_email = mailer,
			to = [my_recipient],
		)

		message.attach_alternative(html_message, "text/html")
		message.send()
		return render(request, "heirs_holding_app/thanks.html")

	return render(request, 'heirs_holding_app/index.html')