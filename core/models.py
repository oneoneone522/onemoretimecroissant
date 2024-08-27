from django.db import models
from django.core.exceptions import ValidationError

class Carousel(models.Model):
    name = models.CharField()
    image = models.ImageField(upload_to='core_images')

    def __str__(self):
        return self.name
class Notification(models.Model):
    notice = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.notice
    
class News(models.Model):
    name = models.CharField()
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='core_images')
    def __str__(self):
        return self.name
    
class Storeimg(models.Model):
    image = models.ImageField(upload_to='core_images')
    the_big = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.the_big:
            # 检查是否已经存在一个 the_big=True 的对象
            existing = Storeimg.objects.filter(the_big=True).exclude(pk=self.pk)
            if existing.exists():
                raise ValidationError("已經有一個對象被設置為True，無法再設置另一個對象為True。")
        
        super().save(*args, **kwargs)  # 保存当前对象

    def __str__(self):
        return f"Storeimg {self.id} - Big: {self.the_big}"