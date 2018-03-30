from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import contactForm


# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        email = form.cleaned_data['email']

        subject = 'message form mysite.com'
        message = '%s %s %s' % (' Name: ' + name, '\n comment: ' + comment, '\n Email: ' + email)
        emailFrom = email
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, [emailTo], fail_silently=True)
        send_mail('Contact submitted', 'Thank you for your feedback', emailFrom, [email], fail_silently=True)
        form = None
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you"
    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request, template, context)
