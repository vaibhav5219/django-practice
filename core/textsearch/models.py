from django.db import models


class TextSearchTags(models.Model):
    tag = models.CharField(max_length=100)

    class Meta:
        db_table = 'textsearch_tags'

class TextSearchProduct(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.CharField(max_length=100, null = True , blank=True)
    sku = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=1000)
    tags = models.ManyToManyField(TextSearchTags)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'textsearch_Product'