from django.db import models

# Create your models here.
class Filmview(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='movie/film',blank=True,null=True)
    def __str__(self):
        return self.name
