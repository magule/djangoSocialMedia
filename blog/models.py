from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse #i guess after creating a post instead of redirect this is being used
# Create your models here.

from django.db import transaction
from django.db.models import F, Max

from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from PIL import Image

#--------------------------------------------------------------------------------------------------------------------------------------

"""class Konum(models.Model):
    konumum = models.CharField(max_length=100)


    def __str__(self):
        return self.konumum


    def get_absolute_url(self):
        return reverse('home')

"""

#--------------------------------------------------------------------------------------------------------------------------------------


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="")
    #content = RichTextField(blank=True, null=True )
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #if is deleted than delete their posts 
    location = models.CharField(max_length=100, default="")
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='blog_posts')
    #this is a new one add to models 
    mood = models.CharField(max_length=20, default="")



    #categories = models.ManyToManyField('Category')
    #konum = models.CharField(max_length=100, default="")




    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



#--------------------------------------------------------------------------------------------------------------------------------------

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


#--------------------------------------------------------------------------------------------------------------------------------------


"""

class History(models.Model):
    id = models.PositiveIntegerField(primary_key=True)       
    history = models.IntegerField(default=0)

    def save(self):
        with transaction.atomic():
            count = History.objects.count()

            objects = History.objects.all()
            if count > 100:
                objects[0].delete()
                if count > 1:
                    objects.update(id=F('id') - 1)

            if not self.id and count > 0:
                objects = objects.refresh_from_db()  # Update QuerySet
                self.id = objects.annotate(max_count=Max('id')).max_count + 1
            elif not self.id and count == 0:
                self.id = 1

            self.save()

"""
