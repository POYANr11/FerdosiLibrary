from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Personnel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()
    biography = RichTextField()
    education = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='personnel_images/')

    def __str__(self):
        return self.name
