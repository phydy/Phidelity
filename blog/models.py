from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

CHOICES =(
    ('fx','Forex'),
    ('bc', 'crypto'),
    ('ix', 'indices'),
    ('cm', 'commodities'),
    ('ed', 'educational')
)
# Create your models here.
class Post(models.Model):
    global CHOICES
    title = models.CharField(max_length=150)
    #snipet = models.TextField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    written_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='blog-pics')
    category = models.CharField(default= CHOICES[0], max_length=50, choices= CHOICES)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_commented']
    
    def __str__(self):
        return self.name
