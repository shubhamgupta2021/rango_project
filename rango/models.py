from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=180 , unique = True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length= 255, unique= True)
    views = models.IntegerField(default=0)
    url  = models.URLField()

    def __unicode__(self):
        return self.title
