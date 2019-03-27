from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from mysite'
        email_from = form.cleaned_data['email']
        message = 'name:\t{}\nemail:\t{}\nmessage:\t{}'.format(name, email_from, comment)
        email_to = [settings.EMAIL_HOST_USER]

        send_mail(
            subject,
            message,
            email_from,
            [email_to, ],
            fail_silently=False,
        )

        title = 'Message sent.'
        confirm_message = 'Thank you for messaging us. We will reply shortly.'
        form = None

    context = {'title': title,
               'form': form,
               'confirm_message': confirm_message, }

    template = 'contact/contact.html'
    return render(request, template, context)
