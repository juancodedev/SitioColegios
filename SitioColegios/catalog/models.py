import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.

class SchoolType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Description = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Description
        
class state_province(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NameSP = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.NameSP)      

class School(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=40)
    #Score = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True) #models.FloatField(null=True, blank=True, default=None) #, validators=[MaxValueValidator(5), MinValueValidator(1)]) #models.FloatField(null=True, blank=True, default=None)
    #Score = models.IntegerField('Evaluacion de la escuela',null=True,blank=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    ImageMD = models.ImageField(upload_to='static/img/modal', max_length=100)
    ImageProfile = models.ImageField(upload_to='static/img/profile', max_length=100)
    Address = models.CharField(max_length=60)
    State_Province = models.ForeignKey(state_province, on_delete=models.CASCADE) # relacion muchos a uno
    Phone = models.CharField(max_length=12)
    Type = models.ForeignKey(SchoolType, on_delete=models.CASCADE)
    Review = models.TextField(max_length=2000)

    def __str__(self):
        return str(self.Name)


class Ratings(models.Model):
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    #Score = models.IntegerField(choices=RATING)
    Score = models.IntegerField('Evaluacion de la escuela',null=True,blank=True,validators=[MinValueValidator(1), MaxValueValidator(5)])
    Schools = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
    #comment = models.TextField('Comentario asociado a la escuela',max_length=500,blank=True)

    def __str__(self):
         return str(self.User)
        #return

    def display_School(self):
        return self.Schools.Name
        #', '.join([ Schools.Name for Schools in self.Schools.all()[:3] ])
    display_School.short_description = 'Escuela'

    def get_user(self):
        return self.User.Name+' '+self.User.Last_Name
        #', '.join([ User.Name for User in self.User.all()[:3] ])+' '+ ', '.join([User.Last_Name for User in self.User.all()[:3] ])
    get_user.short_description = 'Usuario'

    def get_email(self):
        return self.User.Email
        #', '.join([ User.Email for User in self.User.all()[:3] ])
    get_email.short_description = 'Email'

class ContactModel(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nombre = models.CharField(max_length=30, default=None)
    Email = models.EmailField(unique=True, default = None)
    Rut = models.CharField(max_length=14, default=None) 
    Region = models.CharField(max_length=50, default=None)
    Comuna = models.CharField(max_length=50, default=None)
    Metodo = models.CharField(max_length=16, default=None)
    Msg = models.TextField(max_length=1000, default=None)
    Newsletter = models.BooleanField(default=False)

    def __srt__(self):
        return self.Nombre
