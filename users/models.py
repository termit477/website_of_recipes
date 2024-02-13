from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True, blank = True)
#     password = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=50, blank = True)
#     last_name = models.CharField(max_length=50, blank = True)
#     email = models.EmailField(max_length=100)
#     birthday = models.DateField()

#     def __str__(self):
#         return f'{self.username} - {self.first_name} {self.last_name}'
   

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.username} Profile'