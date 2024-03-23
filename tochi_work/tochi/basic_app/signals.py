from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import AccountBalance

@receiver(post_save, sender=User)
def create_account_balance(sender, instance, created, **kwargs):
    if created:
        AccountBalance.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_account_balance(sender, instance, **kwargs):
    instance.accountbalance.save()


# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Crisoption, We offer the best trading services'
        message_html = render_to_string('welcome_email_template.html', {'user': instance})
        message_text = strip_tags(message_html)
        from_email = 'services@crisoption.com'  # Replace with your 'from' email
        to_email = [instance.email]
        fail_silently = False

        send_mail(subject, message_text, from_email, to_email, fail_silently, html_message=message_html)

