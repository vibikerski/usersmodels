from django.db import models


class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
