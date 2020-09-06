from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Person name")
    age = models.IntegerField(default=0,
                              help_text="Person age")
    address = models.CharField(max_length=100,
                            help_text="Person address")
    work = models.CharField(max_length=100,
                            help_text="Person work")
