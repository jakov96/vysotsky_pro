from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


def email_notification(data: dict):
    try:
        t = get_template('mail.html')
        html_content = t.render({
            'name': data.get('name', ''),
            'phone': data.get('phone', ''),
        })
        msg = EmailMultiAlternatives(
            data.get('theme', ''),
            html_content,
            settings.EMAIL_HOST_USER,
            settings.EMAIL_ADMIN
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception:
        pass
