from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fam = models.CharField(max_length=64, default=None)
    name = models.CharField(max_length=64, default=None)
    otc = models.CharField(max_length=64, default=None)
    email = models.EmailField(unique=True, default=None)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=254)
    longitude = models.FloatField(max_length=254)
    height = models.IntegerField()

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Post(models.Model):
    NEW, PENDING, ACCEPTED, REJECTED = 'N', 'P', 'A', 'R'
    STATUS_CHOICES = [(NEW, 'New'), (PENDING, 'Pending',), (ACCEPTED, 'Accepted',), (REJECTED, 'Rejected')]

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEW)
    beauty_title = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    other_titles = models.CharField(max_length=254)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    level_spring = models.CharField(max_length=64, blank=True)
    level_summer = models.CharField(max_length=64, blank=True)
    level_autumn = models.CharField(max_length=64, blank=True)
    level_winter = models.CharField(max_length=64, blank=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pereval')
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} {self.title}'


class Images(models.Model):
    title = models.CharField(max_length=254)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    date_added = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
