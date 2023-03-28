from django.db import models

# Create your models here.

class WorksModel(models.Model):
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.name + self.theme







class ExcsModel(models.Model):
    theme = models.CharField(max_length=100)
    modul = models.CharField(max_length=100)

    def __str__(self):
        return self.theme