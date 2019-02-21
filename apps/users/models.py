from django.db import models
import re
import bcrypt
EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):      #note this is really working off top line. class UserManager inherits from models.Model
    def validate(self, form):
        errors = []                            #Manager inherits from models. which are from the import models from django.db

        if len(form['first_name']) < 3:
            errors.append("First name must be at least 3 characters long")
        if len(form['last_name']) < 3:
            errors.append("Last name must be at least 3 characters long")
        if len(form['username']) < 3:
            errors.append("Username must be at least 3 characters long")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Email must be valid")
        if len(form['password']) < 8:
            errors.append("Password must be at least 8 characters long")

        user_list = self.filter(email = form['email'])
        if len(user_list) > 0:
            errors.append("Email already in use")

     

        return errors

    def create_user_with_hashed_password(self, form):
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        user = self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            pw_hash = pw_hash,

        )
        return user


    def login(self, form):
        errors = []

        try: 
            user = self.get(email=form['email']) 
            if not bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                errors.append("Email or password incorrect.")
        except:
            errors.append('Email or Password incorrect')            #security reasons for email or password
        if len(errors) > 0:
            return (False, errors)
        else:
            return (True, user)


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    pw_hash = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)      #difference of auto_now and auto_now_add
    updated_at = models.DateTimeField(auto_now = True)          #add- add current date time to created_at only when its created
    objects = UserManager()
  
    def __str__(self):
        return self.name



#wireframe shows; name, username, password:, confirm password 8 characters, date with calendar