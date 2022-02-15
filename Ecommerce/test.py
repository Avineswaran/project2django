import django
from allauth.account.models import EmailAddress
print(django.get_version())


verified = EmailAddress.objects.filter(verified__contains=True).count()
unverified = EmailAddress.objects.filter(verified__contains=False).count()

print(verified)