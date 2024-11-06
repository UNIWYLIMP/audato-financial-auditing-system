from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Primary Models Initialization.


# User Profiles
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('User Name'), unique=True, max_length=250)
    fullname = models.CharField(_('Full Name'), default="", max_length=250)
    codex = models.CharField(_('Codex'), default="", max_length=250)

    class Meta:
        db_table = 'Universal Profile'


class AuditFile(models.Model):
    file_one = models.FileField(_('Audit File One'), upload_to='audit_file/', null=True, blank=True, default=None)
    file_two = models.FileField(_('Audit File two'), upload_to='audit_file/', null=True, blank=True, default=None)
    response = models.CharField(_('Audit File Two'), max_length=3000, default="")
    profile = models.ForeignKey('CustomUser', on_delete=models.CASCADE, default=1)


class BinSaver(models.Model):
    file_one = models.FileField(_('Audit File One'), upload_to='audit_file/', null=True, blank=True, default=None)
    file_two = models.FileField(_('Audit File two'), upload_to='audit_file/', null=True, blank=True, default=None)
