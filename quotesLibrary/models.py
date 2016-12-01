from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'authors'


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.quote

    class Meta:
        verbose_name_plural = 'quotes'

