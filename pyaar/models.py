from django.db import models

# Create your models here.

class Animal(models.Model):
    def __str__(self):
        return self.Animal_category
    Animal_category = models.CharField(max_length=200)
    adopted_date = models.DateTimeField("Adoption Date")
    category_id = models.IntegerField()


class Details(models.Model):
    def __str__(self):
        return self.category_details
    category_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    category_details = models.CharField(max_length=200)