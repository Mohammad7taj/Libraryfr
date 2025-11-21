from django.db import models
import uuid

class Author(models.Model):
    first_name = models.CharField(max_length=50, default='...')
    last_name = models.CharField(max_length=50, default='...')
    birthdate = models.DateField()
    biografi = models.TextField(blank=True)
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    kholase = models.TextField(default='kh')
    cover = models.ImageField(upload_to='ket', default='default.jpg')
    pages = models.PositiveSmallIntegerField(default=0)
    creat_at = models.DateTimeField(auto_now_add=True)
    ubdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

