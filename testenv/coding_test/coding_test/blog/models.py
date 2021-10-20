from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = (('Technology', 'Technology'), ('News', 'News'),
                        ('Sports', 'Sports'))
    cover = models.FileField(null=True)
    cover2 = models.FileField(null=True)
    slug = models.SlugField(unique=True)
    text = models.TextField(default='')
    text2 = models.TextField(default='')

    quote = models.TextField(default='')
    quote_name = models.TextField(default='')
    l_heading = models.CharField(max_length=2000, default='')
    l_heading_text = models.CharField(max_length=2000, default='')
    s_heading = models.CharField(max_length=2000, default='')
    s_heading_text = models.CharField(max_length=2000, default='')
    text2 = models.TextField(default='')
     
    title = models.CharField(max_length=2000)
    
    author = models.CharField(max_length=2000, default='')
    category = models.CharField(max_length=2000, choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField()
    tag_1=models.CharField(max_length=2000, default='')
    tag_2=models.CharField(max_length=2000, default='')
    tag_3=models.CharField(max_length=2000, default='')
    
    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return self.title
