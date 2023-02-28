# from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
# from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import PostCategory
# from django.conf import settings
from .tasks import send_notify


# def send_notify(preview, pk, title, subscribers):
#     html_content = render_to_string(
#         'post_created.html',
#         {
#             'Название': title,
#             'Текст': preview,
#             'Ссылка': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(subject=title, body='', from_email=settings.DEFAULT_FROM_EMAIL, to=subscribers)
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            emails += [s.email for s in subscribers]

        send_notify.delay(instance.preview(), instance.pk, instance.title, emails)
