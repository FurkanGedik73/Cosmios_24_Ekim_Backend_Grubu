from django.db import models

# Create your models here.

class Todo(models.Model):

    PRIORITY =(
        (1, "High"),
        (2, "Medium"),
        (3, "Low")
    )

    task = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add= True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task} - {self.priority}"
    
