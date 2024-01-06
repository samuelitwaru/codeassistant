from django.db import models

# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=128)
    plural = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
    def search_fields(self):
        return self.field_set.filter(is_search_field=True).all()
    
    def filter_fields(self):
        return self.field_set.filter(is_filter_field=True).all()

    def column_fields(self):
        return self.field_set.filter(is_column_field=True).all()

class Field(models.Model):
    name = models.CharField(max_length=128)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    is_search_field = models.BooleanField(default=False)
    is_filter_field = models.BooleanField(default=True)
    is_column_field = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Template(models.Model):
    content = models.TextField()