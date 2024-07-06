from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='static/media/member_photos/', null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Plot(models.Model):
    objects = None
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    plot_number = models.CharField(max_length=10)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='static/media/plot_photos/', null=True, blank=True)

class Event(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    photo = models.ImageField(upload_to='static/media/event_photos/', null=True, blank=True)

class Resource(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField()
    resource_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership_fee = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

