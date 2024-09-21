# Its basically the data base of django
from django.db import models

class Feedback(models.Model):
    title = models.CharField(max_length=10)
    desc = models.TextField()

    # def __str__(self):
    #     return self.title

class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    # phone = models.models.PhoneNumberField(_("10"))
    

#makemigrations are the check point just like commi int github
#a model is not created till u not create a app in settings.py 'home.apps.HomeConfig'