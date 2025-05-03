from sib_api_v3_sdk import TransactionalEmailsApi, Configuration, ApiClient
from sib_api_v3_sdk.rest import ApiException
from sib_api_v3_sdk.models import SendSmtpEmail, SendSmtpEmailSender, SendSmtpEmailTo
from django.conf import settings
from django.core.exceptions import ValidationError


def send_email_via_brevo(subject, html_content, recipient_email):
    """Send an email using Brevo SMTP transactional API."""
    configuration = Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_client = ApiClient(configuration)
    api_instance = TransactionalEmailsApi(api_client)

    email = SendSmtpEmail(
        sender=SendSmtpEmailSender(email=settings.BREVO_EMAIL),
        to=[SendSmtpEmailTo(email=recipient_email)],
        subject=subject,
        html_content=html_content,
    )

    try:
        api_instance.send_transac_email(email)
    except ApiException as e:
        raise ValidationError({
            "error": "Failed to send email via Brevo.",
            "details": str(e)
        })
