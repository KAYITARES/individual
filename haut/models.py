from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images

class Staff(models.Model):
    image = models.ImageField(upload_to='staff/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.name
    def save_staff(self):
        self.save()

    @classmethod
    def get_all_staff(cls):
        all_staff = Staff.objects.all()
        return all_staff

class Registor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    email = models.EmailField()
    faculty = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name
    def save_registor(self):
        self.save()
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()