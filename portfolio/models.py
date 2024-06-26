from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=120)
    portfolio_type = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='portfolio/')
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    complete_date = models.DateField()
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

#Email
from django.db import models

class EmailMessage(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    subject = models.CharField(max_length = 3000)
    Message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

