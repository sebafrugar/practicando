from django.db import models
import re
from django.db.models.deletion import CASCADE


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'El nombre debe tener al menos 2 caracteres'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'El apellido debe tener al menos 2 caracteres'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['register_email']):    
            errors['register_email'] = "La dirección de correo electrónico debe ser válida."
        if len(postData['password']) < 6:
            errors['password'] = 'El password debe tener al menos 8 caracteres'
        if postData['password'] != postData['confirm']:
            errors['password'] = "La contraseña debe ser la misma"
        return errors
    def login_validator(self, postData):
        errors ={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):    
            errors['login_email'] = "La dirección de correo electrónico debe ser válida."
        if len(postData['login_password']) < 6:
            errors['login_password'] = 'El password debe tener al menos 8 caracteres'
        return errors
class QuoteManager(models.Manager):       
    def quote_validator(self, postData):
        errors ={}
        if len(postData['quoted_by']) < 2:
            errors['quoted_by'] = 'Quoted by debe tener 2 o más caracteres.'
        if len(postData['message']) < 10:
            errors['message'] = 'El mensaje debe tener 10 o más caracteres'
        return errors
    def edit_validator(self, postData):
        errors ={}
        if len(postData['quoted_by']) < 2:
            errors['quoted_bye'] = 'Quoted by debe tener 2 o más caracteres.'
        if len(postData['message']) < 10:
            errors['message'] = 'El mensaje debe tener 10 o más caracteres'
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=500)
    date_of_birth= models.DateField(blank=False, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)  
    objects = UserManager()
    def __str__(self):
        return f"<{self.first_name} {self.last_name} {self.email}  {self.id}>"

#class Quote(models.Model):
   # quoted_by= models.CharField(null=False,max_length=60)
  #  message= models.TextField(null=False)
  #  uploaded_by=models.ForeignKey(User, related_name="quotes_uploaded", on_delete=CASCADE)
   # user_who_like= models.ManyToManyField(User, related_name="favorite_quotes")
  #  objects = QuoteManager()
  #  def __str__(self):
        return f"<{self.quoted_by} {self.message} {self.id}>"

class Comentario(models.Model):
    name = models.CharField(max_length=45)
    comentario = models.TextField(max_length=150)
