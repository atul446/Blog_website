from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES=(
        ('Technology','Technology'),
        ('News','News'),
        ('Sports','Sports')
    )
    cover= models.FileField()
    title= models.CharField(max_length=2000)
    category=models.CharField(max_length=2000,choices=CATEGORY_CHOICES)
    created_date=models.DateTimeField()
    text= models.TextField()
    
    def _str_(self):
        return self.title