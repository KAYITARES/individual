from django.db import models

# Create your models here.
# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     def __str__(self):
#         return self.image
    
#     def save_image(self):
#         self.save()

# class Staff(models.Model):
#     image = models.ImageField(upload_to='images/')
#     name = models.charField(max_length=50)
#     title = models.charField(max_length=50)
#     post = models.charField(max_length=50)
#     def __str__(self):
#         return self.name
#     def save_staff(self):
#         self.save()

# class Registor(models.model):
#     first_name = models.charField(max_length=50)
#     last_name = models.charField(max_length=50)
#     gender = models.charField(max_length=50)
#     email = models.EmailField()
#     faculty = models.charField(max_length=50)
#     department = models.charField(max_length=50)
#     session = models.charField(max_length=50)
#     def __str__(self):
#         return self.first_name
#     def save_registor(self):
#         self.save()
