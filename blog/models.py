import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Period(models.Model):
    pay_period = models.CharField(max_length=4)

    def __str__(self):
        return self.pay_period

class Forced(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    ops_inits = models.CharField(max_length=2, default="")
    original_shift = models.CharField(max_length=4)
    forced_shift = models.CharField(max_length=4)
    shift_date = models.DateField()

    def __str__(self):
        return self.ops_inits
