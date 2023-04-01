from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    profil_pic = models.ImageField(null=True, blank=True,upload_to=None, height_field=None,width_field=None, max_length=100)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    # def save(self, *args, **kwargs):
    #       self.password = make_password(self.password)
    #       super(CustomUser, self).save(*args, **kwargs)




class TAG(models.Model):
    tags = models.CharField(max_length=30)
   # todo = models.ManyToManyField(Todo)

    def __str__(self):
        return self.tags


class Todo(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=800, blank=True, null=True)
    Due_date = models.DateField(blank=True, null=True)

    class Status(models.TextChoices):
        TODO = 'todo', _('Todo')
        IN_PROGRESS = 'in_progress', _('In_Progress')
        COMPLETED = 'completed', _('Completed')


    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    Created_Date = models.DateField(auto_now_add=True)
    Updated_Date = models.DateField(blank=True, null=True)
    tag_name = models.ManyToManyField(TAG)


    def __str__(self):
        return self.Title 




