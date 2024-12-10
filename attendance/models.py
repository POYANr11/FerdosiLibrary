from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User.username} - {self.timestamp}"
