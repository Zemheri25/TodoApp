from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    PRIORITY = (
        ("1", "High"),
        ("2", "Medium"),
        ("3", "Low"),
    )
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY)
    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title