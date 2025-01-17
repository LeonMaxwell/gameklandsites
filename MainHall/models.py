from django.db import models


# Create your models here.

class AboutMainHall(models.Model):
    id_room = 2
    name_room = models.CharField(max_length=20)
    about_room = models.TextField(max_length=56)
    image_room = models.ImageField(upload_to='main_hall_media')

    def __str__(self):
        return self.name_room