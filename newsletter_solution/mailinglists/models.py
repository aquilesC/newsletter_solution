import uuid as uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class MailingList(models.Model):
    """MailingList is the building block of a newsletter. People subscribe to malinglists on different websites, campaigns are sent
    to malinglists of people. Each list accumulates some basic statistics on open rate and click rate, which are built
    averaging all the campaigns sent.
    """

    uuid = models.CharField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(_('name'), max_length=127)
    slug = models.SlugField(_('list URL'), unique=True)

    subscribers = models.PositiveIntegerField(_('subscribers'), default=0)
    open_rate = models.PositiveIntegerField(_('open rate'), default=0)
    click_rate = models.PositiveIntegerField(_('click rate'), default=0)

    date_created = models.DateTimeField(_('created'), auto_now_add=True)

    contact_email_address = models.EmailField(_('contact email address'), blank=True)

    campaign_default_from_name = models.CharField(_('default from name'), max_length=50)
    campaign_default_from_email = models.EmailField(_('default from email'), blank=False)
    campaign_default_subject = models.CharField(_('default subject'), max_length=100)

    class Meta:
        verbose_name = _('list')
        verbose_name_plural = _('malinglists')

    def __str__(self):
        return self.name


