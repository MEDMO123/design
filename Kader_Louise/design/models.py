from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    adresse=models.CharField(max_length=100)
    telephone=models.CharField(max_length=10)
    def __str__(self):
         return self.username

    
class Collection(models.Model):
    nom_collection=models.CharField(max_length=100)
    Description=models.CharField(max_length=250)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.nom_collection

class Modele(models.Model):
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)
    num_modele=models.IntegerField(default=0)
    nom_modele=models.CharField(max_length=100)
    genre=models.CharField(max_length=10)
    taille=models.CharField(max_length=5)
    modele=models.ImageField(upload_to='media')
    modele1=models.ImageField(upload_to='media')
    modele2=models.ImageField(upload_to='media')
    description =models.CharField(max_length=250)
    prix=models.IntegerField(default=0)
    disponible=models.BooleanField(default=False)    
    def __str__(self):
        return f"{self.num_modele}_{self.nom_modele}"


class Accessoire(models.Model):
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)    
    num_accessoire=models.IntegerField(default=0)
    nom_accessoire=models.CharField(max_length=100)
    genre=models.CharField(max_length=5)   
    modele=models.ImageField(upload_to='media')
    modele1=models.ImageField(upload_to='media')
    modele2=models.ImageField(upload_to='media')
    description =models.CharField(max_length=250)
    prix=models.IntegerField(default=0)
    disponible=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.num_accessoire}_{self.nom_accessoire}"


class Rdv(models.Model):
    client=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    date_rdv=models.DateField()
    objet=models.CharField(max_length=250)
    confirme=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.date_rdv}_{self.client.username}"


class Commandemodele (models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    modele=models.ForeignKey(Modele,on_delete=models.CASCADE)  
    date=models.DateField(auto_now=True)    
    reception=models.CharField(max_length=30)
    taille=models.CharField(max_length=5,default='M')
    confirme=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.client.username}_{self.date}_{self.confirme}"

class Commandeaccessoire (models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    accessoire=models.ForeignKey(Accessoire,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    reception=models.CharField(max_length=30)    
    confirme=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.client.username}_{self.date}"
 