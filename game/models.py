from django.db import models

class Author(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(max_length=255)
    
class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE, blank=True)