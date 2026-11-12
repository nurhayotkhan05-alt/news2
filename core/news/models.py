from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="blogs/")
    author = models.CharField(max_length=100, default='Admin')
    author_image = models.ImageField(upload_to="author_img/")
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


def small_img(value):
    img = Image.open(value)
    if img.width != 272  and img.height != 270:
        raise ValidationError('Small image ki size: 272x270 hona chahiye')

def medium_img(value):
    img = Image.open(value)
    if img.width != 566 and img.height != 258:
        raise ValidationError('Medium image ki size: 566x258 hona chahiye')

def large_img(value):
    img = Image.open(value)
    if img.width != 566 and img.height != 546:
        raise ValidationError('Large image ki size: 566x546 hona chahiye')


class HeroBlog(models.Model):
    img1 = models.ImageField(
        upload_to="hero_img/",
        validators=[large_img],
        help_text="566x546",
    )
    img2 = models.ImageField(
        upload_to="hero_img/",
        validators=[medium_img],
        help_text="546x258",
    )
    img3 = models.ImageField(
        upload_to="hero_img/",
        validators=[small_img],
        help_text="272x270",
    )
    img4 = models.ImageField(
        upload_to="hero_img/",
        validators=[small_img],
        help_text="272x270",
    )
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    title3 = models.CharField(max_length=255)
    title4 = models.CharField(max_length=255)

    def __str__(self):
        return "HeroBlog"
