from django.db import models

class News(models.Model):
    image_url = models.URLField(max_length=500, blank=True, null=True)
    title =  models.CharField(max_length=500, blank=True, null=True)
    link_address = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'news'
    
