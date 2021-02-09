from django.db import models

# Create your models here.

class Feedback(models.Model):
      name=models.CharField(max_length=50)
      email=models.CharField(max_length=100)
      message=models.CharField(max_length=500)
      date= models.DateField()


      def __str__(self):
            return self.name
