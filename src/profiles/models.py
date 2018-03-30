from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.money import Money


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='profile_image', blank=True)
    website = models.URLField(default='', blank=True)
    bio = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)
    Credit = MoneyField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinMoneyValidator(0),
            MaxMoneyValidator(1500),
            MinMoneyValidator(Money(0, 'NOK')),
            MaxMoneyValidator(Money(900, 'NOK')),
            MinMoneyValidator({'EUR': 100, 'USD': 0}),
            MaxMoneyValidator({'EUR': 1000, 'USD': 500}),
        ])

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile.objects.create(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
