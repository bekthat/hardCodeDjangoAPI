from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.product.name}"


class Lesson(models.Model):
    product = models.ForeignKey(Product, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Group(models.Model):
    product = models.ForeignKey(Product, related_name='groups', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_users = models.IntegerField()
    max_users = models.IntegerField()
    users = models.ManyToManyField(User, related_name='user_groups', blank=True)

    def __str__(self):
        return f"{self.name} - {self.product.name}"