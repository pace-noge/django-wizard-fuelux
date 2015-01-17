from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)



class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class ArticleProperty(models.Model):
    name = models.CharField(max_length=25)
    property = models.CharField(max_length=100)
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return "%s: %s" % (self.name, self.property)

    class Meta:
        ordering = ('name', )