from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")

class Post(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    date = models.DateTimeField(default=timezone.now)
    category =  models.CharField(max_length=255, default='coding')
    body = models.TextField(null= True, blank= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,related_name = 'blogpost_like', blank=True)
    #featured_image = CloudinaryField('image', default='placeholder')
    
    class Meta:
        ordering = ['-date']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
   

    class Meta:
        ordering = ["created_on"]
   

    def __str__(self):
        return '%s-%s' % (self.post.title, self.name)
        #return f"Comment {self.body} by {self.name}"



