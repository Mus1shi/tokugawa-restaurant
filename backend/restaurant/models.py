from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Chef(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    chef = models.ForeignKey('Chef', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0.00)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"commentaire de {self.name} (Posté le {self.created_at})"

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    date = models.DateField()
    people = models.IntegerField()
    time = models.TimeField()
    content = models.TextField()

    def __str__(self):
        return f"Réservation de {self.name} le {self.date} à {self.time}"

