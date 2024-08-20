from django.db import models

class Carousel(models.Model):
    name = models.CharField()
    image = models.ImageField(upload_to='core_images')

    def __str__(self):
        return self.name
class News(models.Model):
    name = models.CharField()
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='core_images')
    def __str__(self):
        return self.name
class Storeimg(models.Model):
    image = models.ImageField(upload_to='core_images')
    the_big = models.BooleanField(default=False)