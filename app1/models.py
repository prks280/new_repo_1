from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Father(models.Model):
    name = models.CharField(max_length=20)
    nominee = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name