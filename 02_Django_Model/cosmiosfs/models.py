from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    about = models.TextField()
    email = models.EmailField(unique=True)
    register_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="students")

    class Meta:
        ordering = ["-number"]
        verbose_name = "Öğrenciler"
        verbose_name_plural = "Öğrenci"

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.email} - {self.number}"

