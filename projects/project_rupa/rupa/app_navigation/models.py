from django.db import models

class User(models.Model):

    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<User object: {self.email}>"
