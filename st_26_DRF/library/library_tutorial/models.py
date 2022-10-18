from django.db import models

class Author (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book (models.Model):
    name = models.CharField(max_length=50)
    publish_year = models.IntegerField()
    authors = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f" {self.name} {self.publish_year}"
