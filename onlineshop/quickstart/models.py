from django.db import models
 
  


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    price = models.IntegerField(default=False) 

    class Meta:
        ordering = ['created']