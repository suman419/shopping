from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200,db_index=True)
#     slug = models.SlugField(max_length=100, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name



class Product(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    #product_id = models.CharField(max_length=20, null=False)
    image = models.ImageField(blank =True)
    url = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
        

        