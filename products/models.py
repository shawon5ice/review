from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/',default='images/default.png')
    body = models.TextField()
    url = models.URLField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.srtptime('%b %d %Y')


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name
