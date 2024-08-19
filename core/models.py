from django.db import models

class Carousel(models.Model):
    name = models.TextField(max_length=10, blank=True)
    image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return self.name