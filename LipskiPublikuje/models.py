from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    CATEGORY_CHOICES = [
        ('finanse', 'Finanse'),
        ('sztuka', 'Sztuka'),
        ('ciekawostki', 'Ciekawostki'),
        ('polityka', 'Polityka'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="ciekawostki")
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    Fullimage = models.ImageField(upload_to='fullimages/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
        return self.title

class Comments(models.Model):
    nickname = models.CharField(max_length=50)
    CommentContent = models.TextField()
    pub_date = models.DateTimeField()
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')

class AboutMe(models.Model):
    content = RichTextField(blank=True, null=True)
    social_facebook = models.URLField(max_length=200, default='https://www.facebook.com')
    social_twitter = models.URLField(max_length=200, default='https://www.twitter.com')
    social_git = models.URLField(max_length=200, default='https://www.github.com')

