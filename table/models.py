from django.db import models

class Table(models.Model):
    date = models.DateTimeField()
    
    name = models.CharField(blank=True, max_length=200)
    
    count = models.PositiveIntegerField()
    
    distance = models.PositiveIntegerField()