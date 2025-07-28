from django.db import models
class images(models.Model):
    name= models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False, primary_key=True)

    def __str__(self):
        return self.email

# Create your models here.
