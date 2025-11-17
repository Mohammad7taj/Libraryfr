from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    biografi = models.TextField(blank=True)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = 'نویسنده'

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    published_day = models.DateField()
    pages = models.PositiveSmallIntegerField(default=0)
    creat_at = models.DateTimeField(auto_now_add=True)
    ubdate = models.DateTimeField(auto_now=True)



