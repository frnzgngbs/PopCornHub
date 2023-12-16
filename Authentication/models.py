from django.db import models


class User(models.Model):
    userID = models.AutoField(primary_key= True)
    username = models.CharField(max_length=40, null=False, unique=True)
    password = models.CharField(max_length=40, null=False)
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, max_length=40,  null=False)

    def __str__(self):
        return self.username
