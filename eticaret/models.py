from django.db import models

# Create your models here.


class Website(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.TextField()
    commission = models.FloatField()
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {}'.format(self.name, self.website)
