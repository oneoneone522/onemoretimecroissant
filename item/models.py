from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order']

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    hot_item = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Box(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    hot_item = models.BooleanField(default=False)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name
    

