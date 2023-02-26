from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import PostCategory
from django.conf import settings


def send_notify(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created.html',
        {
            'Название': title,
            'Такст': preview,
            'Ссылка': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(subject=title, body='', from_email=settings.DEFAULT_FROM_EMAIL, to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        print('Я сигнал!')
        categories = instance.postCategory.all()
        emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            emails += [s.email for s in subscribers]

        send_notify(instance.preview, instance.pk, instance.title, emails)


        # emails = User.objects.filter(
        #     subscriptions__category=instance.postCategory
        # ).values_list('email', flat=True)
        #
        # subject = f'Новая публикация в категории {instance.postCategory}'
        #
        # text_content = (
        #     f'Заголовок: {instance.title}\n'
        #     f'Превью: {instance.texp.preview}\n\n'
        #     f'Ссылка на публикацию: http://127.0.0.1{instance.get_absolute_url()}'
        # )
        # html_content = (
        #     f'Заголовок: {instance.title}<br>'
        #     f'Превью: {instance.texp.preview}<br><br>'
        #     f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        #     f'Ссылка на публикацию</a>'
        # )
        # for email in emails:
        #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
        #     msg.attach_alternative(html_content, "text/html")
        #     msg.send()
