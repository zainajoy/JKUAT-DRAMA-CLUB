from django.db import models

# Create your models here.
class Member (models.Model): # name of the table 
    registrationnumber = models.CharField(max_length=20,primary_key=True) # strings with a max length in character of 20
    name = models.CharField(max_length=200) # strings with a max length in character of 200
    course = models.CharField(max_length=255) # strings with a max length in character of 255
    department = models.CharField(max_length=255) # strings with a max length in character of 255
    photo = models.ImageField(upload_to='member-photos/', blank=True) # image field for member photos
    phonenumber = models.CharField(max_length=15,null=True,blank=True) # strings with a max length in character of 15
    date_joined = models.DateField(auto_now_add=True) # date field
    def __str__(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='events/', blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

         