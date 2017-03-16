from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    important = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name