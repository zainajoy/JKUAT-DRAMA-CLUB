from django.db import models

# Create your models here.
class member (models.Model): # name of the table 
    registrationnumber = models.CharField(max_length=20,primary_key=True) # strings with a max length in character of 20
    name = models.CharField(max_length=200) # strings with a max length in character of 200
    course = models.CharField(max_length=255) # strings with a max length in character of 255
    department = models.CharField(max_length=255) # strings with a max length in character of 255
    photo = models.ImageField(upload_to='member-photos/', blank=True) # image field for member photos
    phonenumber = models.CharField(max_length=15,null=True,blank=True) # strings with a max length in character of 15
    date_joined = models.DateField(auto_now_add=True) # date field
    def __str__(self):
        return self.name
    
class event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='events/', blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
class payments(models.Model):
    member = models.ForeignKey(member, on_delete=models.CASCADE)
    amount = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    mpese_receipt_number = models.CharField(max_length=50, null=True, blank=True)
    date_paid = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.amount}"         