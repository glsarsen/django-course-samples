from django.db import models

# Create your models here.
class PhoneBook(models.Model):
    name = models.CharField("Name", max_length=20)
    lastname = models.CharField("Lastname", max_length=20)
    email = models.EmailField("Email")
    phone = models.CharField("Tel", max_length=20)
    about = models.CharField("About", max_length=70)

    def __str__(self):
        return f"{self.name} : {self.lastname} : {self.email} : {self.phone} : {self.about}"