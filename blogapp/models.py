from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/" )
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
       return  str(self.user)

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255, unique= False)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="blog_posts")
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    content = models.TextField()
    likes = models.ManyToManyField(User,related_name = 'blogpost_like', blank= True)
    update_date = models.DateTimeField(default=timezone.now)
    snippet = models.CharField(max_length=255)
    blog_image = models.ImageField(null=True, blank=True, upload_to="images/" )
    
    
    
    class Meta:
        ordering = ['-date_posted']

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    content = models.TextField()
    date_posted =  models.DateTimeField(default=timezone.now)

    class Meta:
      ordering = ["-date_posted"]
   
    def __str__(self):
      #  return '%s-%s' % (self.post.title, self.name)
        return f"Comment {self.content} by {self.name}"